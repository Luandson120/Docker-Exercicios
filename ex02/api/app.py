from flask import Flask, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )

@app.route("/")
def home():
    return "API conectada ao banco via Docker! 🚀"

@app.route("/add")
def add_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mensagens (id SERIAL PRIMARY KEY, texto TEXT)")
    cur.execute("INSERT INTO mensagens (texto) VALUES ('Hello from Docker + Postgres!')")
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "ok", "mensagem": "Dado inserido no banco!"})

@app.route("/listar")
def listar_dados():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM mensagens")
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(dados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
