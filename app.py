from flask import Flask, render_template
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # โหลดค่าจากไฟล์ .env

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="10.199.8.40",
        port="3308",
        user="phiraphat.ni",
        password="683380049-5",
        database="phiraphat.ni_ticket_db"
    )

@app.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM concerts")
    concerts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", concerts=concerts)

if __name__ == "__main__":
    app.run(debug=True)