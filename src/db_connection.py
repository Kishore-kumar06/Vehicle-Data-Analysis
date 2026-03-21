import mysql.connector
from src.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, AUTH_PLUGIN


def get_connection():
    """Return an open MySQL connection."""
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        auth_plugin=AUTH_PLUGIN
    )
    return connection
