from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

@app.route('/db')
def check_db():
    try:
        conn = psycopg2.connect(
            host="db",
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        return "Connected to Database!"
    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)