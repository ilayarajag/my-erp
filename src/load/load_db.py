# src/load/load_db.py

import psycopg2
from config.db_config import get_connection

def load(df):
    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO users (id, name) VALUES (%s, %s)",
            (row["id"], row["name"])
        )

    conn.commit()
    cursor.close()
    conn.close()