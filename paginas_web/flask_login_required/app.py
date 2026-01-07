from flask import Flask, render_template, session, request, jsonify, redirect, url_for
from database import create_table, init_db
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = "232d.dejncdkjc34.4"

create_table()

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"success": False, "redirect": "/login"}), 401
        return func(*args, **kwargs)
    return wrapper

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username", "").strip()
        password = data.get("password")

        try:
            conn = init_db()
            c = conn.cursor()
            c.execute("INSERT INTO users(username, password) VALUES(?,?)", (username, password))
            conn.commit()
            conn.close()

            return jsonify({"success": True, "message": "Registered User"})
        except sqlite3.IntegrityError:
            return jsonify({"success": False, "message": "Existing user"})
        
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()

        username = data.get("username", "").strip()
        password  = data.get("password")

        conn = init_db()
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()


        if user:
            session["user_id"] = user[0]
            return jsonify({"success": True, "message": "Login correct", "redirect": "/dashboard"})
        else:
            return jsonify({"success": False, "message": "Username or password incorrect"})

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    session.pop("user_id", None)

    return redirect(url_for("index"))

@app.route("/test")
def test():
    return jsonify(dict(session))


if __name__ == "__main__":
    app.run(debug=True)