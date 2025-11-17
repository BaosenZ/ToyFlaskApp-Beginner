from flask import Flask, render_template, request, redirect, flash
from tasks import trigger_all_jobs
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "your-secret-key"

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")


@app.route("/")
def index():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user="root",
        password="password",
        database="jobs_db",
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, smiles, concentration FROM files")
    files = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", files=files)


@app.route("/trigger-all", methods=["POST"])
def trigger_all():
    trigger_all_jobs.delay()
    flash("Job submitted to Perlmutter!")
    return redirect("/")
