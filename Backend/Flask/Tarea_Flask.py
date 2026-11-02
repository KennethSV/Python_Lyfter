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

valid_statuses = [
    "Pending",
    "In Progress",
    "Completed"
]

project_dir = os.path.join(os.path.dirname(__file__))
tasks_path = os.path.join(project_dir, "tasks.json")

def read_data():
    if not os.path.exists(tasks_path):
        return []
    
    with open(tasks_path, "r") as f:
        return json.load(f)

def save_data(tasks):
    with open(tasks_path, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = read_data()
             
    filtered_tasks = tasks
    filtered_by_status = request.args.get("status")

    if filtered_by_status:
        filtered_tasks = list(
            filter(lambda task: task["status"].lower() == filtered_by_status.lower(), filtered_tasks)
        )
    return jsonify({"data": filtered_tasks}), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = read_data()
    
    data = request.json    
    
    existing_ids = {task["id"] for task in tasks}

    if "id" in data:
        if data["id"] in existing_ids:
            return jsonify({"message": "Task ID already exists, try another ID"}), 400
                
        if type(data["id"]) is not int:
            return jsonify({"message": "The ID must be an integer (int)"}), 400

        if "title" not in data or str(data["title"]).strip() == "":
            return jsonify({"message": "Task does not include a valid title"}), 400

        if "description" not in data or str(data["description"]).strip() == "":
            return jsonify({"message": "Task does not include a valid description"}), 400

        if "status" not in data:
            return jsonify({"message": "Task does not include status"}), 400

        if data["status"] not in valid_statuses:
            return jsonify({"message": f"Invalid status. Must be one of: {valid_statuses}"}), 400
        
        new_task = {
                "id": data["id"],
                "title": data["title"],
                "description": data["description"],
                "status": data["status"]
        }
        
        tasks.append(new_task)
        save_data(tasks)
        
        return jsonify(new_task), 201
        
    else:
        return jsonify({"message": "Task ID not included"}), 400

@app.route("/tasks/<int:id>", methods=["PATCH"])
def update_task(id):
    tasks = read_data()

    new_data = request.json
    task_found = False

    for task in tasks:
        if task["id"] == id:
            if "title" in new_data:
                task["title"] = new_data["title"]
            if "description" in new_data:
                task["description"] = new_data["description"]
            if "status" in new_data:
                if new_data["status"] not in valid_statuses:
                    return jsonify({"message": f"Invalid status. Must be one of: {valid_statuses}"}), 400
                else:
                    task["status"] = new_data["status"]
            task_found = True
            break

    if task_found:
        save_data(tasks)
        return jsonify(task), 200
    
    else:
        return jsonify({"message": "Task not found"}), 404

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    tasks = read_data()
    
    new_tasks = [t for t in tasks if t["id"] != id]
        
    if len(tasks) == len(new_tasks):
        return jsonify({"message": "Task not found"}), 404
        
    save_data(new_tasks)
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == "__main__":
    if not os.path.exists(tasks_path):
        with open(tasks_path, "w") as f:
            json.dump([], f)

    app.run(host="localhost", port=8001, debug=True)