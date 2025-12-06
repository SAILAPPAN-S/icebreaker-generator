import sqlite3
import os

# /.../ICEBREAKER-AI/src
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level (project root), then into db/profiles.db
DB_PATH = os.path.join(BASE_DIR, "..", "db", "profiles.db")

def get_profile_by_id(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, location, interests, bio FROM user_profiles WHERE id=?", (user_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "age": row[2],
        "location": row[3],
        "interests": row[4].split(","),
        "bio": row[5]
    }
