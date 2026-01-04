from flask import Flask, request, render_template, jsonify
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
            return jsonify({"mensaje": "Datos vacios"})
    except ValueError as e:
        return jsonify({"mensaje: ": f"Error: {e}"})

    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO personas(nombre,edad) VALUES (?,?)", (nombre,edad))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Persona guardada correctamente"})


if __name__ == "__main__":
    app.run(debug=True) 