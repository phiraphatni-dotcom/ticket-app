import os
import mysql.connector
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        port=int(os.environ.get("DB_PORT", 13686)),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        ssl_disabled=False,
        ssl_verify_identity=False
    )

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM concerts")
        concerts = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template("index.html", concerts=concerts)
    except Exception as e:
        return f"Database Connection Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)