import mysql.connector
from src.db_config import Data_Cred

def get_connection():
    """Return an open MySQL connection."""

    connection = mysql.connector.connect(
        host=Data_Cred.DB_HOST,
        port=Data_Cred.DB_PORT,
        user=Data_Cred.DB_USER,
        password=Data_Cred.DB_PASSWORD,
        database=Data_Cred.DB_NAME,
        auth_plugin=Data_Cred.AUTH_PLUGIN
    )
    return connection
