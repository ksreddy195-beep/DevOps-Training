import psycopg2
from psycopg2 import Error
from app.config import Config

def get_db_connection():
    try:
        return psycopg2.connect(**Config.DB_CONFIG)
    except Error as e:
        raise Exception(f"Database connection failed: {e}")