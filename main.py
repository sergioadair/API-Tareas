from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)

    def serialize(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "fecha_creacion": self.fecha_creacion
        }
    
with app.app_context():
    db.create_all()


@app.route("/")
def root():
    return """<pre>
GET     /tareas     leer todas las tareas existentes.
POST    /tareas     crear una nueva tarea.
GET     /tareas/ID  leer una tarea por su ID.
PUT     /tareas/ID  actualizar una tarea por su ID.
DELETE  /tareas/ID  eliminar una tarea por su ID.
</pre>"""

@app.route("/tareas", methods=['GET'])
def leer_tareas():
    tareas = Tareas.query.all()
    lista_tareas = [tarea.serialize() for tarea in tareas]
    return jsonify(lista_tareas), 200

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.json
    nueva_tarea = Tareas(
        titulo = datos.get('titulo'),
        descripcion = datos.get('descripcion'),
        estado = datos.get('estado', False)
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify(nueva_tarea.serialize()), 201

@app.route('/tareas/<id>', methods=['GET'])
def leer_tarea(id):
    tarea = Tareas.query.get_or_404(id)
    return jsonify(tarea.serialize()), 200

@app.route('/tareas/<id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tareas.query.get_or_404(id)
    datos = request.json
    tarea.titulo = datos.get('titulo', tarea.titulo)
    tarea.descripcion = datos.get('descripcion', tarea.descripcion)
    tarea.estado = datos.get('estado', tarea.estado)
    db.session.commit()
    return jsonify(tarea.serialize()), 200

@app.route('/tareas/<id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = Tareas.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea eliminada exitosamente'}), 200


if __name__ == "__main__":
    app.run(debug=True)