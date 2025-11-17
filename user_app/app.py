from flask import Flask, request, redirect, render_template
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    smiles = request.form["smiles"]
    concentration = float(request.form["concentration"])
    conn = mysql.connector.connect(
        host=DB_HOST,
        user="root",
        password="password",
        database="jobs_db",
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO files (smiles, concentration) VALUES (%s, %s)",
        (smiles, concentration),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")
