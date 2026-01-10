'''
- Crea un API con `Flask` de que permita un `CRUD` (Create, Read, Update, Delete) de `tareas`.
- Cada `tarea` debe tener:
    - `Identificador`
    - `Título`
    - `Descripción`
    - `Estado` (Por Hacer, En Progreso o Completada),
- El API debe tener endpoints para:
    1. Obtener `tareas`.
        1. Esta debe tener un query parameter **opcional** para filtrarlas por `Estado`.
    2. Crear `tareas`.
    3. Editar `tareas`.
    4. Eliminar `tareas`.
- Todos los datos deberán guardarse en un archivo JSON.
    - Cada *endpoint* debe leer del archivo, y escribir en él (en caso de ser crear, editar o eliminar).
- Además, debe de validar que:
    1. No se puedan agregar `tareas` con identificadores ya existentes.
    2. No se puedan agregar `tareas` sin nombre.
    3. No se pueden agregar `tareas` sin descripción.
    4. No se puedan agregar `tareas` sin estado.
    5. No se puedan agregar `tareas` con un estado invalido.

1. Investigue cómo crear *endpoints* en `Flask` usando un `MethodView`
    - Puedes leer la documentación de esta clase acá: https://flask.palletsprojects.com/en/3.0.x/views/#method-dispatching-and-apis
2. Haga una *refactorización* del ejercicio de arriba en otro archivo utilizando esta implementación
    - *Refactorizar se refiere a re-estructurar código ya existente*
3. Añadir un sistema simple de autenticación a la API de tareas
- Requisitos:
    - Cree un endpoint `/login` que reciba un usuario y contraseña
    - Si las credenciales son correctas, devuelva un token (puede ser una cadena generada aleatoriamente)
    - Guarde el token en un diccionario en memoria o en un archivo `.json`
    - Todos los endpoints del CRUD deben requerir el token en los headers
        - Si no se incluye o es incorrecto, devolver un error `401 Unauthorized`
- *Tip:* Use el header: `Authorization: Bearer <token>`
'''

from flask import Flask, jsonify, request, Response, json
from flask.views import MethodView
import datetime
import os
from functools import wraps
import jwt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kgb'

estados_validos = [
    "Por hacer",
    "En progreso",
    "Completado"
]

user_pass = [
    {"user": "Kenneth", "pass":"Cisco123!"},
    {"user": "Sammy", "pass":"Cisco123!"},
    {"user": "Daniela", "pass":"Cisco123!"}
]

tareas_path = "/Users/ksolorzanovalverde/Documents/GitHub/Python_Lyfter/Backend/Flask/tareas.json"
tareas_token = "/Users/ksolorzanovalverde/Documents/GitHub/Python_Lyfter/Backend/Flask/token.json"

def leer_datos():
    if not os.path.exists(tareas_path):
        return []
    try:
        with open(tareas_path, "r") as f:
            return json.load(f)
    except Exception:
        return []
    
def leer_token():
    if not os.path.exists(tareas_token): 
        return {}
    try:
        with open(tareas_token, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def guardar_datos(tareas):
    with open(tareas_path, "w") as f:
        json.dump(tareas, f, indent=4)

def guardar_token(nuevo_token, user):
    diccionario_tokens = leer_token()
    
    if isinstance(nuevo_token, bytes):
        nuevo_token = nuevo_token.decode('utf-8') 
    diccionario_tokens[nuevo_token] = user 
    
    with open(tareas_token, "w") as f:
        json.dump(diccionario_tokens, f, indent=4)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({"message": "Token faltante. Use header 'Authorization: Bearer <token>'"}), 401
        
        try:
             token_recibido = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({"message": "Formato de token inválido"}), 401
        
        tokens_validos = leer_token()
        
        if token_recibido not in tokens_validos:
            return jsonify({"message": "Token inválido o no encontrado"}), 401

        return f(*args, **kwargs)
    return decorated

class Login(MethodView):
     
    def post(self):
        data = request.json
        
        if not data or "user" not in data or "pass" not in data:
            return jsonify({"message": "Faltan credenciales"}), 400

        incoming_user = data["user"]
        incoming_pass = data["pass"]

        for user_record in user_pass:
            if user_record["user"] == incoming_user and user_record["pass"] == incoming_pass:
                token = jwt.encode({
                    'user': incoming_user,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }, app.config['SECRET_KEY'], algorithm="HS256")
                guardar_token(token, incoming_user)
                return jsonify({'token': token}), 200

        return jsonify({"message": "Credenciales inválidas"}), 401


class Tareas(MethodView):

    decorators = [token_required]

    def get(self):
        tareas = leer_datos()

        tareas_filtradas = tareas
        tareas_filtradas_por_estado = request.args.get("estado")

        if tareas_filtradas_por_estado:
            tareas_filtradas = list(
                filter(lambda show: show["estado"] == tareas_filtradas_por_estado, tareas_filtradas)
            )
        return {"data": tareas_filtradas}

    def post(self):
        tareas = leer_datos()
        data = request.json

        try:
            for tarea in tareas:
                if tarea["id"] == data["id"]:
                        return jsonify({"message": "ID de tarea pre-existente, intentar con otro ID"}), 400

            if "id" not in data:
                    raise ValueError("Tarea no incluye el identificador")
                
            if type(data["id"]) is not int:
                    raise ValueError("El ID debe ser un número entero (int)")

            if "titulo" not in data:
                    raise ValueError("Tarea no incluye titulo")

            if "descripcion" not in data:
                    raise ValueError("Tarea no incluye descripcion")

            if "estado" not in data:
                    raise ValueError("Tarea no incluye estado")

            if data["estado"] not in estados_validos:
                    return jsonify({"message": f"Estado invalido. Debe ser uno de: {estados_validos}"}), 400
                
            nueva_tarea = {
                "id": data["id"],
                "titulo": data["titulo"],
                "descripcion": data["descripcion"],
                "estado": data["estado"]
            }
                
            tareas.append(nueva_tarea)
            guardar_datos(tareas)

            return jsonify(tareas), 201
            
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 528

    def patch(self, tarea_id):
        
        tareas = leer_datos()
        data = request.json

        tarea_encontrada = False

        for tarea in tareas:
            if tarea["id"] == tarea_id:
                if "titulo" in data:
                    tarea["titulo"] = data["titulo"]
                if "descripcion" in data:
                    tarea["descripcion"] = data["descripcion"]
                if "estado" in data:
                    if data["estado"] not in estados_validos:
                        return jsonify({"message": f"Estado invalido. Debe ser uno de: {estados_validos}"}), 400
                    else:
                        tarea["estado"] = data["estado"]
                tarea_encontrada = True
                break

        if tarea_encontrada:
            guardar_datos(tareas)
            return jsonify(tarea), 200
        
        else:
            return jsonify({"message": "Tarea no encontrada"}), 404

    def delete(self, tarea_id):

        tareas = leer_datos()
        data = request.json

        tareas_nuevas = [t for t in tareas if t["id"] != tarea_id]
        
        if len(tareas) == len(tareas_nuevas):
            return jsonify({"message": "Tarea no encontrada"}), 404
        
        guardar_datos(tareas_nuevas)
        return jsonify({"message": "Tarea eliminada exitosamente"}), 200

if __name__ == "__main__":
    if not os.path.exists(tareas_path):
        with open(tareas_path, "w") as f:
            json.dump([], f)

    tareas_view = Tareas.as_view('tareas_api')
    login_view = Login.as_view('login_api')

    app.add_url_rule('/login', view_func=login_view, methods=['POST'])
    app.add_url_rule('/tareas', view_func=tareas_view, methods=['GET', 'POST'])
    app.add_url_rule('/tareas/<int:tarea_id>', view_func=tareas_view, methods=['PATCH', 'DELETE'])

    app.run(host="localhost", port=8001, debug=True)