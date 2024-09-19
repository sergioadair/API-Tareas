from flask import Flask, jsonify, render_template, request
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

    def __repr__(self) -> str:
        return self.titulo

    def serialize(self) -> dict:
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
    return render_template('index.html')

@app.route("/tareas", methods=['GET'])
def leer_tareas():
    tareas = Tareas.query.all()
    lista_tareas = [tarea.serialize() for tarea in tareas]
    return jsonify(lista_tareas), 200, {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.form
    nueva_tarea = Tareas(
        titulo = datos.get('titulo'),
        descripcion = datos.get('descripcion'),
        estado = datos.get('estado') == 'true'
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify(nueva_tarea.serialize()), 201



if __name__ == "__main__":
    app.run(debug=True)