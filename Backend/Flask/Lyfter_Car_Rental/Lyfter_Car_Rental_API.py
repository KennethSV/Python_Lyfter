'''
Tarea 3: Creación del API

Con los scripts anteriores, cree un API que sea capaz de realizar las siguientes tareas:
- Creación:
    - Crear un usuario nuevo
    - Crear un automóvil nuevo
    - Crear un alquiler nuevo
- Modificación
    - Cambiar el estado de un automovil
    - Cambiar el estado de un usuario
    - Completar un alquiler
    - Cambiar el estado de un alquiler
    - Flagear un usuario como moroso
- Listado
    - Listar todos los usuarios
    - Listar todos los automóviles
    - Listar todos los alquileres
    - Todos los endpoints de listado deben aceptar filtros por cualquier columna de la tabla que consulten.
      Ejemplos: /usuarios?username=sofia.jimenez  /automoviles?modelo=corolla  /alquileres?estado=activo

Antes de correr el API se deben ejecutar los scripts de la carpeta SQL (01 al 04).
Requiere: pip install flask psycopg2-binary
'''

from flask import Flask, jsonify, request
from flask.views import MethodView
from functools import wraps
import datetime
import os
import psycopg2
from psycopg2 import errors
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "postgres")
}

schema = "lyfter_car_rental"

estados_usuario = ["Activo", "Inactivo"]
estados_automovil = ["Disponible", "Alquilado", "Mantenimiento", "Deshabilitado"]
estados_alquiler = ["Activo", "Completado", "Cancelado"]

# Columnas por las que se puede filtrar cada listado (el password nunca se expone)
columnas_usuarios = ["usuario_id", "nombre", "correo", "username", "fecha_nacimiento", "estado", "moroso"]
columnas_automoviles = ["automovil_id", "marca", "modelo", "anio_fabricacion", "estado"]
columnas_alquileres = ["alquiler_id", "usuario_id", "automovil_id", "fecha_alquiler", "fecha_devolucion", "estado"]


def obtener_conexion():
    return psycopg2.connect(**db_config)

def formatear_filas(filas):
    resultado = []
    for fila in filas:
        fila = dict(fila)
        for llave, valor in fila.items():
            if isinstance(valor, (datetime.date, datetime.datetime)):
                fila[llave] = valor.isoformat()
        resultado.append(fila)
    return resultado

def ejecutar_consulta(query, params=None):
    conexion = obtener_conexion()
    try:
        with conexion:
            with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return formatear_filas(cursor.fetchall())
    finally:
        conexion.close()

def construir_filtros(columnas_validas):
    # Cada query param se compara (sin importar mayúsculas) contra su columna.
    # Se puede usar % como comodín, por ejemplo: ?fecha_alquiler=2026-11%
    condiciones = []
    valores = []

    for columna, valor in request.args.items():
        if columna not in columnas_validas:
            raise ValueError(f"Filtro invalido '{columna}'. Debe ser uno de: {columnas_validas}")
        condiciones.append(f"CAST({columna} AS TEXT) ILIKE %s")
        valores.append(valor)

    if condiciones:
        return " WHERE " + " AND ".join(condiciones), valores
    return "", valores

def campo_vacio(data, campo):
    return campo not in data or str(data[campo]).strip() == ""

def obtener_estado(data, estados_validos):
    if "estado" not in data:
        raise ValueError("No se incluyó el estado")

    estado = str(data["estado"]).strip().capitalize()
    if estado not in estados_validos:
        raise ValueError(f"Estado invalido. Debe ser uno de: {estados_validos}")
    return estado

def manejar_errores(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except LookupError as ex:
            return jsonify(message=str(ex)), 404
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except errors.UniqueViolation:
            return jsonify(message="Ya existe un registro con ese valor único (correo o username)"), 400
        except psycopg2.OperationalError:
            return jsonify(message="No se pudo conectar a la base de datos"), 500
        except Exception as ex:
            return jsonify(message=str(ex)), 500
    return decorated

def cambiar_estado_alquiler(alquiler_id, nuevo_estado):
    # Cambia el estado de un alquiler y mantiene sincronizado el estado del automóvil
    conexion = obtener_conexion()
    try:
        with conexion:
            with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    f"SELECT estado, automovil_id FROM {schema}.Alquileres WHERE alquiler_id = %s FOR UPDATE",
                    (alquiler_id,)
                )
                alquiler = cursor.fetchone()

                if not alquiler:
                    raise LookupError("Alquiler no encontrado")

                if alquiler["estado"] == nuevo_estado:
                    raise ValueError(f"El alquiler ya se encuentra en estado {nuevo_estado}")

                if nuevo_estado in ["Completado", "Cancelado"]:
                    if alquiler["estado"] != "Activo":
                        raise ValueError(f"Solo un alquiler Activo puede pasar a {nuevo_estado}")

                    cursor.execute(
                        f"""UPDATE {schema}.Alquileres
                            SET estado = %s,
                                fecha_devolucion = CASE WHEN %s = 'Completado' THEN CURRENT_TIMESTAMP END
                            WHERE alquiler_id = %s
                            RETURNING *""",
                        (nuevo_estado, nuevo_estado, alquiler_id)
                    )
                    alquiler_actualizado = cursor.fetchone()

                    cursor.execute(
                        f"UPDATE {schema}.Automoviles SET estado = 'Disponible' WHERE automovil_id = %s",
                        (alquiler["automovil_id"],)
                    )

                else:
                    # Reactivar un alquiler solo si el automóvil sigue disponible
                    cursor.execute(
                        f"SELECT estado FROM {schema}.Automoviles WHERE automovil_id = %s FOR UPDATE",
                        (alquiler["automovil_id"],)
                    )
                    automovil = cursor.fetchone()

                    if automovil["estado"] != "Disponible":
                        raise ValueError(f"El automóvil no está disponible (estado: {automovil['estado']})")

                    cursor.execute(
                        f"""UPDATE {schema}.Alquileres
                            SET estado = 'Activo', fecha_devolucion = NULL
                            WHERE alquiler_id = %s
                            RETURNING *""",
                        (alquiler_id,)
                    )
                    alquiler_actualizado = cursor.fetchone()

                    cursor.execute(
                        f"UPDATE {schema}.Automoviles SET estado = 'Alquilado' WHERE automovil_id = %s",
                        (alquiler["automovil_id"],)
                    )

                return formatear_filas([alquiler_actualizado])[0]
    finally:
        conexion.close()


class Usuarios(MethodView):

    decorators = [manejar_errores]

    def get(self):
        where, valores = construir_filtros(columnas_usuarios)
        usuarios = ejecutar_consulta(
            f"SELECT {', '.join(columnas_usuarios)} FROM {schema}.Usuarios{where} ORDER BY usuario_id",
            valores
        )
        return jsonify({"data": usuarios}), 200

    def post(self):
        data = request.get_json(silent=True) or {}

        for campo in ["nombre", "correo", "username", "password", "fecha_nacimiento"]:
            if campo_vacio(data, campo):
                return jsonify({"message": f"Usuario no incluye {campo}"}), 400

        try:
            datetime.date.fromisoformat(str(data["fecha_nacimiento"]))
        except ValueError:
            return jsonify({"message": "La fecha_nacimiento debe tener el formato YYYY-MM-DD"}), 400

        estado = obtener_estado(data, estados_usuario) if "estado" in data else "Activo"

        nuevo_usuario = ejecutar_consulta(
            f"""INSERT INTO {schema}.Usuarios (nombre, correo, username, password, fecha_nacimiento, estado)
                VALUES (%s, %s, %s, crypt(%s, gen_salt('bf')), %s, %s)
                RETURNING {', '.join(columnas_usuarios)}""",
            (data["nombre"], data["correo"], data["username"], data["password"], data["fecha_nacimiento"], estado)
        )
        return jsonify(nuevo_usuario[0]), 201

class Usuario_estado(MethodView):

    decorators = [manejar_errores]

    def patch(self, usuario_id):
        data = request.get_json(silent=True) or {}
        estado = obtener_estado(data, estados_usuario)

        usuario = ejecutar_consulta(
            f"UPDATE {schema}.Usuarios SET estado = %s WHERE usuario_id = %s RETURNING {', '.join(columnas_usuarios)}",
            (estado, usuario_id)
        )

        if not usuario:
            return jsonify({"message": "Usuario no encontrado"}), 404
        return jsonify(usuario[0]), 200

class Usuario_moroso(MethodView):

    decorators = [manejar_errores]

    def patch(self, usuario_id):
        # Por defecto marca al usuario como moroso; con {"moroso": false} se quita la marca
        data = request.get_json(silent=True) or {}
        moroso = data.get("moroso", True)

        if type(moroso) is not bool:
            return jsonify({"message": "El campo moroso debe ser true o false"}), 400

        usuario = ejecutar_consulta(
            f"UPDATE {schema}.Usuarios SET moroso = %s WHERE usuario_id = %s RETURNING {', '.join(columnas_usuarios)}",
            (moroso, usuario_id)
        )

        if not usuario:
            return jsonify({"message": "Usuario no encontrado"}), 404
        return jsonify(usuario[0]), 200


class Automoviles(MethodView):

    decorators = [manejar_errores]

    def get(self):
        where, valores = construir_filtros(columnas_automoviles)
        automoviles = ejecutar_consulta(
            f"SELECT {', '.join(columnas_automoviles)} FROM {schema}.Automoviles{where} ORDER BY automovil_id",
            valores
        )
        return jsonify({"data": automoviles}), 200

    def post(self):
        data = request.get_json(silent=True) or {}

        for campo in ["marca", "modelo", "anio_fabricacion"]:
            if campo_vacio(data, campo):
                return jsonify({"message": f"Automóvil no incluye {campo}"}), 400

        if type(data["anio_fabricacion"]) is not int or not 1950 <= data["anio_fabricacion"] <= 2100:
            return jsonify({"message": "El anio_fabricacion debe ser un número entero (int) entre 1950 y 2100"}), 400

        estado = obtener_estado(data, estados_automovil) if "estado" in data else "Disponible"

        if estado == "Alquilado":
            return jsonify({"message": "Un automóvil nuevo no puede crearse como Alquilado"}), 400

        nuevo_automovil = ejecutar_consulta(
            f"""INSERT INTO {schema}.Automoviles (marca, modelo, anio_fabricacion, estado)
                VALUES (%s, %s, %s, %s)
                RETURNING {', '.join(columnas_automoviles)}""",
            (data["marca"], data["modelo"], data["anio_fabricacion"], estado)
        )
        return jsonify(nuevo_automovil[0]), 201

class Automovil_estado(MethodView):

    decorators = [manejar_errores]

    def patch(self, automovil_id):
        data = request.get_json(silent=True) or {}
        estado = obtener_estado(data, estados_automovil)

        if estado == "Alquilado":
            return jsonify({"message": "Para alquilar un automóvil use POST /alquileres"}), 400

        automovil_actual = ejecutar_consulta(
            f"SELECT estado FROM {schema}.Automoviles WHERE automovil_id = %s",
            (automovil_id,)
        )

        if not automovil_actual:
            return jsonify({"message": "Automóvil no encontrado"}), 404

        if automovil_actual[0]["estado"] == "Alquilado":
            return jsonify({"message": "El automóvil está alquilado, primero complete el alquiler"}), 400

        automovil = ejecutar_consulta(
            f"""UPDATE {schema}.Automoviles SET estado = %s
                WHERE automovil_id = %s AND estado <> 'Alquilado'
                RETURNING {', '.join(columnas_automoviles)}""",
            (estado, automovil_id)
        )

        if not automovil:
            return jsonify({"message": "El automóvil está alquilado, primero complete el alquiler"}), 400
        return jsonify(automovil[0]), 200


class Alquileres(MethodView):

    decorators = [manejar_errores]

    def get(self):
        where, valores = construir_filtros(columnas_alquileres)
        alquileres = ejecutar_consulta(
            f"SELECT {', '.join(columnas_alquileres)} FROM {schema}.Alquileres{where} ORDER BY alquiler_id",
            valores
        )
        return jsonify({"data": alquileres}), 200

    def post(self):
        data = request.get_json(silent=True) or {}

        for campo in ["usuario_id", "automovil_id"]:
            if campo not in data:
                return jsonify({"message": f"Alquiler no incluye {campo}"}), 400
            if type(data[campo]) is not int:
                return jsonify({"message": f"El {campo} debe ser un número entero (int)"}), 400

        conexion = obtener_conexion()
        try:
            with conexion:
                with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(
                        f"SELECT estado, moroso FROM {schema}.Usuarios WHERE usuario_id = %s",
                        (data["usuario_id"],)
                    )
                    usuario = cursor.fetchone()

                    if not usuario:
                        return jsonify({"message": "Usuario no encontrado"}), 404
                    if usuario["estado"] != "Activo":
                        return jsonify({"message": "El usuario no está activo"}), 400
                    if usuario["moroso"]:
                        return jsonify({"message": "El usuario está marcado como moroso"}), 400

                    # FOR UPDATE evita que dos alquileres tomen el mismo automóvil al mismo tiempo
                    cursor.execute(
                        f"SELECT estado FROM {schema}.Automoviles WHERE automovil_id = %s FOR UPDATE",
                        (data["automovil_id"],)
                    )
                    automovil = cursor.fetchone()

                    if not automovil:
                        return jsonify({"message": "Automóvil no encontrado"}), 404
                    if automovil["estado"] != "Disponible":
                        return jsonify({"message": f"El automóvil no está disponible (estado: {automovil['estado']})"}), 400

                    cursor.execute(
                        f"""INSERT INTO {schema}.Alquileres (usuario_id, automovil_id)
                            VALUES (%s, %s)
                            RETURNING *""",
                        (data["usuario_id"], data["automovil_id"])
                    )
                    nuevo_alquiler = cursor.fetchone()

                    cursor.execute(
                        f"UPDATE {schema}.Automoviles SET estado = 'Alquilado' WHERE automovil_id = %s",
                        (data["automovil_id"],)
                    )

            return jsonify(formatear_filas([nuevo_alquiler])[0]), 201
        finally:
            conexion.close()

class Alquiler_estado(MethodView):

    decorators = [manejar_errores]

    def patch(self, alquiler_id):
        data = request.get_json(silent=True) or {}
        estado = obtener_estado(data, estados_alquiler)

        alquiler = cambiar_estado_alquiler(alquiler_id, estado)
        return jsonify(alquiler), 200

class Alquiler_completar(MethodView):

    decorators = [manejar_errores]

    def patch(self, alquiler_id):
        # Confirma la devolución: el alquiler pasa a Completado y el automóvil a Disponible
        alquiler = cambiar_estado_alquiler(alquiler_id, "Completado")
        return jsonify(alquiler), 200


if __name__ == "__main__":
    usuarios_view = Usuarios.as_view('usuarios_api')
    usuario_estado_view = Usuario_estado.as_view('usuario_estado_api')
    usuario_moroso_view = Usuario_moroso.as_view('usuario_moroso_api')
    automoviles_view = Automoviles.as_view('automoviles_api')
    automovil_estado_view = Automovil_estado.as_view('automovil_estado_api')
    alquileres_view = Alquileres.as_view('alquileres_api')
    alquiler_estado_view = Alquiler_estado.as_view('alquiler_estado_api')
    alquiler_completar_view = Alquiler_completar.as_view('alquiler_completar_api')

    app.add_url_rule('/usuarios', view_func=usuarios_view, methods=['GET', 'POST'])
    app.add_url_rule('/usuarios/<int:usuario_id>/estado', view_func=usuario_estado_view, methods=['PATCH'])
    app.add_url_rule('/usuarios/<int:usuario_id>/moroso', view_func=usuario_moroso_view, methods=['PATCH'])
    app.add_url_rule('/automoviles', view_func=automoviles_view, methods=['GET', 'POST'])
    app.add_url_rule('/automoviles/<int:automovil_id>/estado', view_func=automovil_estado_view, methods=['PATCH'])
    app.add_url_rule('/alquileres', view_func=alquileres_view, methods=['GET', 'POST'])
    app.add_url_rule('/alquileres/<int:alquiler_id>/estado', view_func=alquiler_estado_view, methods=['PATCH'])
    app.add_url_rule('/alquileres/<int:alquiler_id>/completar', view_func=alquiler_completar_view, methods=['PATCH'])

    app.run(host="localhost", port=8001, debug=True)
