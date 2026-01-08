from flask import Flask, request, render_template, jsonify
from database import create_table, init_db

app = Flask(__name__)

create_table()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/person", methods=["POST"])
def save_person():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data received"}), 400

    name = data.get("name").strip()
    age = data.get("age")
    note = data.get("note")

    try:
        age = int(age)
        note = int(note)

        if not age or not note or name.strip() == "":
            return jsonify({"message": "No data received"})
        if age <= 0 or note <= 0:
            return jsonify({"message": "Age or note invalid"})
        
    except(ValueError, TypeError):
        return jsonify({"message": f"Error: {ValueError}"})
    
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO people(name, age, note) VALUES(?,?,?)", (name,age,note))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved person"})

@app.route("/person", methods=["GET"])
def get_person():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT id,name,age,note FROM people")
    people = c.fetchall()
    conn.close()

    list = []


    for person in people:
        list.append({"id": person[0], "name": person[1], "age": person[2], "note": person[3]})

    return jsonify(list)

@app.route("/person/<int:id>", methods=["DELETE"])
def delete_person(id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM people WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Deleted person"})

@app.route("/person", methods=["DELETE"])
def delete_all():
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM people")
    conn.commit()
    conn.close()

    return jsonify({"message": "People eliminated"})

@app.route("/person/<int:id>", methods=["PUT"])
def update_person(id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data received"})

    name = data.get("name").strip()
    age = data.get("age")
    note = data.get("note")

    try:
        age = int(age)
        note = int(note)

        if not age or not note or name.strip() == "":
            return jsonify({"message": "No data received"})
        if age <= 0 or note <= 0:
            return jsonify({"message": "Age or note invalid"})
    
    except (ValueError, TypeError):
        return jsonify({"message": f"Error: {ValueError}"})
    
    conn = init_db()
    c = conn.cursor()
    c.execute("UPDATE people SET name=?, age=?, note=? WHERE id=?", (name,age,note,id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Updated person"})

if __name__ == "__main__":
    app.run(debug=True)