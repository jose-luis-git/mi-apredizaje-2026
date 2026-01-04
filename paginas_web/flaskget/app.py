from flask import Flask,render_template,request,jsonify
from database import crear_tabla, init_db

app = Flask(__name__)

crear_tabla()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/persona", methods=["POST"])
def guardar_persona():
    datos = request.get_json()
    nombre = datos["nombre"]
    edad = datos["edad"]

    try:
        edad = int(edad)
        if not nombre.strip() or not edad:
            return jsonify({"mensaje": "Datos incompletos"})
    except ValueError as e:
        return jsonify({"mensaje": f"Error: {e}"})
    
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO personas(nombre,edad) VALUES(?,?)", (nombre,edad))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Datos guardados correctamente"})


@app.route("/persona", methods=["GET"])
def obtener_persona():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT id,nombre,edad FROM personas")
    personas = c.fetchall()
    conn.close()

    lista = []


    for persona in personas:
        lista.append({"id": persona[0], "nombre": persona[1], "edad": persona[2]})

    return jsonify(lista)
        

@app.route("/persona", methods=["DELETE"])
def borrar_todos():
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM personas")
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Todos los registros fueron eliminados"})


@app.route("/persona/<int:id>", methods=["DELETE"])
def borrar_persona(id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM personas WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": f"Persona con ID {id} fue eliminada"})


if __name__ == "__main__":
    app.run(debug=True)