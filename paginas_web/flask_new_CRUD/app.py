from database import create_table, init_db
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

create_table()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods=["POST"])
def save_user():
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data recived"})

    name = data.get("name").strip()
    email = data.get("email").strip()

    try:
        if name.strip() == "" or email.strip() == "":
            return jsonify({"message": "Name or email empty"})
    except(ValueError, TypeError):
        return jsonify({"message": f"Error{ValueError}"})
    
    conn = init_db()
    c = conn.cursor()
    c.execute("INSERT INTO users(name, email)VALUES(?,?)", (name,email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved user"})

@app.route("/user", methods=["GET"])
def get_user():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT id, name, email FROM users")
    users = c.fetchall()
    conn.close()

    list = []


    for user in users:
        list.append({"id": user[0], "name": user[1], "email": user[2]})
    
    return jsonify(list)

@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Deleted user"})

@app.route("/user", methods=["DELETE"])
def delete_all():
    conn = init_db()
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()

    return jsonify({"message": "All user deleted"})

@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "No data recived"})
    
    name = data.get("name").strip()
    email = data.get("email").strip()

    try:
        if name.strip() == "" or email.strip() == "":
            return jsonify({"message": "Name or email empty"})
    except(ValueError, TypeError):
        return jsonify({"message": f"Error: {ValueError}"})

    conn = init_db()
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name,email,id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Updated user"})

if __name__ == "__main__":
    app.run(debug=True)