from src.db_connection import get_connection
from src.db_config import Data_Cred
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()


def get_payment():
    try:
        data = pd.read_csv(os.getenv("CLEAED_PAYMENT_UPDATER_FILE"), encoding="utf-8" )
        for date, payment_mode in zip(data["date"], data["payment"]):
            yield date, payment_mode

    except Exception as e:
        print(f"Error in reading payment updates: {e}")



def data_updater():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        for date, payment_id in get_payment():
            update_query = """
            UPDATE transactions
            SET payment_id = %s
            WHERE transaction_date = %s AND payment_id IS NULL;
            """
            cursor.execute(update_query, (payment_id, date))
        
        conn.commit()
        print("Payment mode updated successfully.")

    except Exception as e:
        print(f"Error in updating payment mode: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

