from flask import Flask,request,render_template,jsonify
from database import create_table, init_db

app = Flask(__name__)

create_table()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/person", methods=["POST"])
def save_person():
    data = request.get_json()
    name = data["name"]
    age = data["age"]

    try:
        age = int(age)
        if not age or not name.strip():
            return jsonify({"message": "Error empty data"})
    except ValueError as e:
        return jsonify({"message": f"Mistake: {e}"})
    
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO person(name, age) VALUES(?,?)", (name,age))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved person"})

@app.route("/person", methods=["GET"])
def get_person():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT id, name, age FROM person")
    people = c.fetchall()
    conn.close()

    list = []

    
    for person in people:
        list.append({"id" : person[0], "name" : person[1], "age" : person[2]})

    return jsonify(list)

@app.route("/person", methods=["DELETE"])
def delete_people():
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM person")
    conn.commit()
    conn.close()

    return jsonify({"message": "All records delete"})

@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM person WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Eliminated person"})

@app.route("/person/<int:id>", methods=["PUT"])
def update_person(id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data recived"}), 400
    
    name = data.get("name", "").strip()
    age = data.get("age")

    if not name:
        return jsonify({"message": "Name is required"}), 400
    
    try:
        age = int(age)
        if age <= 0:
            return jsonify({"messaje": "Invelid age"}), 400
    except (ValueError, TypeError):
        return jsonify({"message": "Age must be number"}), 400
    
    conn = init_db()
    c = conn.cursor()
    c.execute("UPDATE person SET name=?, age=? WHERE id=?", (name,age,id))

    if c.rowcount == 0:
        conn.close()
        return jsonify({"message": "Person not found"}), 400

    conn.commit()
    conn.close()

    return jsonify({"message": "Person update"})

if __name__ == "__main__":
    app.run(debug=True)