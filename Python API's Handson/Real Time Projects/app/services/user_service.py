from app.db.connection import get_db_connection

def create_user(name, email):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO user_schema.users (name, email) VALUES (%s, %s) RETURNING id;",
        (name, email)
    )
    user_id = cur.fetchone()[0]
    conn.commit()

    cur.close()
    conn.close()
    return user_id


def get_all_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, email FROM user_schema.users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {"id": r[0], "name": r[1], "email": r[2]}
        for r in rows
    ]


def update_user(user_id, name, email):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE user_schema.users SET name=%s, email=%s WHERE id=%s RETURNING id;",
        (name, email, user_id)
    )

    if cur.rowcount == 0:
        return False

    conn.commit()
    cur.close()
    conn.close()
    return True


def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM user_schema.users WHERE id=%s RETURNING id;",
        (user_id,)
    )

    if cur.rowcount == 0:
        return False

    conn.commit()
    cur.close()
    conn.close()
    return True