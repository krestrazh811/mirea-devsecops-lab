from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB_PASSWORD = os.getenv("DB_PASSWORD", "P@ssw0rd")


def get_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/user')
def get_user():
    name = request.args.get('name', '')
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE name = ?", (name, ))
    row = cur.fetchone()
    conn.close

    if row:
        return jsonify({"id": row[0], "name": row[1]})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    debug_mode = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug_mode)
