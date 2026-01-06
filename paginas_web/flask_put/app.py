from flask import Flask,render_template, request, jsonify
from database import create_table, init_db

app = Flask(__name__)

create_table()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/student", methods=["POST"])
def seve_student():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data recived"}), 400

    name = data.get("name", "").strip()
    age = data.get("age")
    note = data.get("note")

    if not name:
        return jsonify({"message": "Name is required"}), 400
    
    try:
        age = int(age)
        note = float(note)

        if age <= 0 or note <= 0:
            return jsonify({"message": "Invalid data"}), 400
    except (ValueError, TypeError):
        return jsonify({"message": "Age must be number"}), 400
    
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO students(name, age, note) VALUES(?,?,?)", (name, age, note))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved student"})

@app.route("/student", methods=["GET"])
def get_student():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT id, name, age, note FROM students")
    students = c.fetchall()
    conn.close()

    list = []


    for student in students:
        list.append({"id": student[0], "name": student[1], "age": student[2], "note": student[3]})

    return jsonify(list)

@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Eliminated student"})

@app.route("/student", methods=["DELETE"])
def delete_students():
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM students")
    conn.commit()
    conn.close()

    return jsonify({"message": "All students deleted"})

@app.route("/student/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data recived"})
    
    name = data.get("name", "").strip()
    age = data.get("age")
    note = data.get("note")

    if not name:
        return jsonify({"message": "Name is required"}), 400
    
    try:
        age = int(age)
        note = float(note)

        if age <= 0 or note <= 0:
            return jsonify({"message": "Invalid data"}), 400
    except (ValueError, TypeError):
        return jsonify({"message": "Data be must number"}), 400
    
    conn = init_db()
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, age=?, note=? WHERE id=?", (name,age,note,id))
   
    if c.rowcount == 0:
        return jsonify({"message": "Person not found"}), 400
   
    conn.commit()
    conn.close()

    return jsonify({"message": "Person update"})

if __name__ == "__main__":
    app.run(debug=True)