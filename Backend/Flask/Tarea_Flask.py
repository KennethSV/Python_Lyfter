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
import os

app = Flask(__name__)

estados_validos = [
    "Por hacer",
    "En progreso",
    "Completado"
]

# tareas_path = "/Users/ksolorzanovalverde/Documents/GitHub/Python_Lyfter/Backend/Flask/tareas.json"

project_dir = os.path.join(os.path.dirname(__file__))
tareas_path = os.path.join(project_dir, "tareas.json")

def leer_datos():
    if not os.path.exists(tareas_path):
        return []
    try:
        with open(tareas_path, "r") as f:
            return json.load(f)
    except Exception:
        return []

def guardar_datos(tareas):
    with open(tareas_path, "w") as f:
        json.dump(tareas, f, indent=4)

@app.route("/tareas", methods=["GET"])

def leer_tareas():

    tareas = leer_datos()
             
    tareas_filtradas = tareas
    tareas_filtradas_por_estado = request.args.get("estado")

    if tareas_filtradas_por_estado:
        tareas_filtradas = list(
            filter(lambda show: show["estado"] == tareas_filtradas_por_estado, tareas_filtradas)
        )
    return jsonify({"data": tareas_filtradas}), 200

@app.route("/tareas", methods=["POST"])

def modificar_tareas():

    tareas = leer_datos()
    
    data = request.json    
    
    id_existente = {tarea["id"] for tarea in tareas}

    if "id" in data:
        try:
            if data["id"] in id_existente:
                return jsonify({"message": "ID de tarea pre-existente, intentar con otro ID"}), 400
                
            if type(data["id"]) is not int:
                return jsonify({"message": f"El ID debe ser un número entero (int)"}), 400

            if "titulo" not in data:
                return jsonify({"message": f"Tarea no incluye titulo"}), 400

            if "descripcion" not in data:
                return jsonify({"message": f"Tarea no incluye descripcion"}), 400

            if "estado" not in data:
                return jsonify({"message": f"Tarea no incluye estado"}), 400

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
            return jsonify(message=str(ex)), 500
        
    else:
        return jsonify({"message": "ID de tarea no incluida"}), 400

@app.route("/tareas/<int:id>", methods=["PATCH"])

def editar_tarea(id):

    tareas = leer_datos()

    new_data = request.json
    tarea_encontrada = False

    for tarea in tareas:
        if tarea["id"] == id:
            if "titulo" in new_data:
                tarea["titulo"] = new_data["titulo"]
            if "descripcion" in new_data:
                tarea["descripcion"] = new_data["descripcion"]
            if "estado" in new_data:
                if new_data["estado"] not in estados_validos:
                    return jsonify({"message": f"Estado invalido. Debe ser uno de: {estados_validos}"}), 400
                else:
                    tarea["estado"] = new_data["estado"]
            tarea_encontrada = True
            break

    if tarea_encontrada:
        guardar_datos(tareas)
        return jsonify(tarea), 200
    
    else:
        return jsonify({"message": "Tarea no encontrada"}), 404

@app.route("/tareas/<int:id>", methods=["DELETE"])

def eliminar_tarea(id):

    tareas = leer_datos()
    
    tareas_nuevas = [t for t in tareas if t["id"] != id]
        
    if len(tareas) == len(tareas_nuevas):
        return jsonify({"message": "Tarea no encontrada"}), 404
        
    guardar_datos(tareas_nuevas)
    return jsonify({"message": "Tarea eliminada exitosamente"}), 200

if __name__ == "__main__":
    if not os.path.exists(tareas_path):
        with open(tareas_path, "w") as f:
            json.dump([], f)

    app.run(host="localhost", port=8001, debug=True)