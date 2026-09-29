from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_NAME = os.getenv("DB_NAME", "appdb")


@app.route("/")
def home():
    return jsonify({
        "application": "Three Tier Flask Application",
        "version": APP_VERSION,
        "status": "running"
    })


@app.route("/api/")
def api_info():
    return jsonify({
        "application": "Three Tier Flask Application",
        "version": APP_VERSION,
        "status": "running"
    })


@app.route("/health")
def health():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        connection.close()

        return jsonify({
            "status": "healthy",
            "database": "connected"
        }), 200

    except Exception as e:

        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }), 503


@app.route("/api/message")
def message():
    return jsonify({
        "message": "Hello from Flask backend!"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
