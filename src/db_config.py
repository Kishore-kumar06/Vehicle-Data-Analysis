import os
from dotenv import load_dotenv

load_dotenv()

class Data_Cred:
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    AUTH_PLUGIN = os.getenv("AUTH_PLUGIN")

    cleaned_data_folder = os.getenv("CLEANED_DATA_FOLDER")

    table_upload_order = os.getenv("TABLE_UPLOAD_ORDER")

