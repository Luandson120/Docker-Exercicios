from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/add")
def add():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mensagens (id SERIAL PRIMARY KEY, texto TEXT)")
    cur.execute("INSERT INTO mensagens (texto) VALUES ('Hello from Docker + Postgres!') RETURNING id;")
    conn.commit()
    inserted_id = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"inserted_id": inserted_id})

@app.route("/list")
def list_messages():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=None)
    cur.execute("SELECT * FROM mensagens ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
