import os
import time
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")

DB_USER = os.environ.get("MYSQL_USER", "appuser")
DB_PASS = os.environ.get("MYSQL_PASSWORD", "apppass")
DB_HOST = os.environ.get("MYSQL_HOST", "db")
DB_NAME = os.environ.get("MYSQL_DATABASE", "college_db")
DB_PORT = os.environ.get("MYSQL_PORT", "3306")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(120), nullable=False)

def wait_for_db(retries=10, delay=3):
    for i in range(retries):
        try:
            db.session.execute("SELECT 1")
            return
        except OperationalError:
            print(f"DB not ready... retry {i+1}/{retries}")
            time.sleep(delay)
    raise Exception("Database connection failed")

@app.before_first_request
def init_db():
    wait_for_db()
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")

        if not (name and email and course):
            flash("Fill all fields!", "error")
            return redirect(url_for("register"))

        if Student.query.filter_by(email=email).first():
            flash("Email already exists!", "error")
            return redirect(url_for("register"))

        student = Student(name=name, email=email, course=course)
        db.session.add(student)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for("students"))

    return render_template("register.html")

@app.route("/students")
def students():
    return render_template("students.html", students=Student.query.all())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
