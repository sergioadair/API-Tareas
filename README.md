# API-Tareas
### API RESTful simple en Flask que permite realizar operaciones CRUD sobre un recurso llamado "Tareas". 

Para instalar los paquetes necesarios:
pip install -r requirements.txt

Para correr el servidor:
python main.py

La API estará corriendo en http://localhost:5000

#### Se pueden probar los endpoints usando curl.

* Crear una nueva tarea: curl -X POST localhost:5000/tareas -H "Content-Type: application/json" -d "{\"titulo\": \"Ejemplo\", \"descripcion\": \"Ejemplo desc.\", \"estado\": false}"

* Leer todas las tareas: curl localhost:5000/tareas

* Leer una tarea por ID: curl localhost:5000/tareas/ID

* Actualizar una tarea:  curl -X PUT localhost:5000/tareas/ID -H "Content-Type: application/json" -d "{\"titulo\": \"Nuevo título\", \"descripcion\": \"Nueva descripción\", \"estado\": true}"

* Eliminar una tarea por ID: curl -X DELETE localhost:5000/tareas/ID
