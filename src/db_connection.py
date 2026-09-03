import mysql.connector
from src.db_config import Data_Cred
from utils.logfiles import setup_logger

logger = setup_logger("db_connection")

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

        return connection
    except mysql.connector.Error as err:
        logger.error(f"Error connecting to MySQL: {err}")
        raise

    
