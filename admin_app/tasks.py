from celery import Celery
import mysql.connector
import os
import time

celery_app = Celery(
    "tasks", broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
)

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")


@celery_app.task
def trigger_all_jobs():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user="root",
        password="password",
        database="jobs_db",
    )
    cursor = conn.cursor()

    cursor.execute("SELECT smiles, concentration FROM files")
    rows = cursor.fetchall()
    print("Submitting full job to Perlmutter:")
    for smiles, concentration in rows:
        print(f"SMILES: {smiles}, Concentration: {concentration}")
    time.sleep(10)  # Simulate processing

    cursor.close()
    conn.close()
