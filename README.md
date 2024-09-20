# API-Tareas
### API RESTful simple en python que permite realizar operaciones CRUD sobre un recurso llamado "Tareas". 

Para instalar los paquetes necesarios:
pip install -r requirements.txt

Para correr el servidor:
python main.py

La API estará corriendo en http://localhost:5000

Se pueden probar los endpoints usando curl.
Crear una nueva tarea: curl -X POST localhost:5000/tareas -H "Content-Type: application/json" -d '{"titulo": "Ejemplo", "descripcion": "Ejemplo desc.", "estado": false}'
