import mysql.connector
from src.db_config import Data_Cred
from utils.logfiles import log_error

log_error("db_connection")

def get_connection():
    """Return an open MySQL connection."""
    try:
        connection = mysql.connector.connect(
                host=Data_Cred.DB_HOST,
                port=Data_Cred.DB_PORT,
                user=Data_Cred.DB_USER,
                password=Data_Cred.DB_PASSWORD,
                database=Data_Cred.DB_NAME,
                auth_plugin=Data_Cred.AUTH_PLUGIN
            )

        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        raise
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed")
    
