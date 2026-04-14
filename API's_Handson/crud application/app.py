from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import Error

server = Flask(__name__)

#database configuration

connection_details = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "satish123",
    "database": "user_login"
}

#function to establish a connection with db
def db_connection():
    try:
        conn = psycopg2.connect(**connection_details)
        return conn
    except Error as e:
        raise Exception(f"database connection failed with error : {e}")
    
#Post the data into db via API

#create user(post)

@server.route("/users", methods=["POST"])
def create_user():
    data = request.json
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_schema.users (name, email) VALUES (%s, %s) RETURNING id; ",(data["name"], data["email"]) )
    user_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({
        "message": f"{user_id}user created successfully",
        "id": user_id
    }), 201

#Get request
@server.route("/users", methods=["GET"])
def get_user():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_schema.users;")
    rows = cur.fetchall()


    cur.close()
    conn.close()

    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return jsonify(users)



# -------------------------------
# UPDATE USER (PUT)
# -------------------------------
@server.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    conn = None
    cur = None

    try:
        data = request.get_json()
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "name and email are required"}), 400

        conn = db_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE user_schema.users SET name=%s, email=%s WHERE id=%s RETURNING id;",
            (data["name"], data["email"], user_id)
        )

        if cur.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        conn.commit()
        return jsonify({"message": "User updated successfully"}), 200

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


# -------------------------------
# DELETE USER (DELETE)
# -------------------------------
@server.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = None
    cur = None
    print(user_id)
    try:
        conn = db_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM user_schema.users WHERE id=%s RETURNING id;",
            (user_id,)
        )

        if cur.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        conn.commit()
        return jsonify({"message": "User deleted successfully"}), 200

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    server.run(port=5000, debug=True)


