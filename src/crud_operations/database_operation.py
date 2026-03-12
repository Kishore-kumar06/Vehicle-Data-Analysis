import mysql.connector as sql
import pandas as pd
import os


file = r"D:\Project\Vehicle-Data-Analysis\source_files\cleaned_files\locations.csv"

def connect_database():
    try:
        db_connection = sql.connect(
            host="localhost",
            user="root",
            password="kum@r1998",
            database="vehicle_expense_analytics",
            port=3306,
            auth_plugin="mysql_native_password"
        )

        if db_connection.is_connected():
            print("Database connection successful")
            return db_connection
        else:
            print("Database connection failed")
            return None
    except sql.Error as err:
        print(f"Database connection failed: {err}")


def fetch_records():
    try:
        database = connect_database()

        if database:
            cursor = database.cursor()
            
            query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'locations';"
            
            cursor.execute(operation=query)
            for col in cursor.fetchall():
                print(col)


    except sql.Error as err:
        print(f"Database connection failed: {err}")

# fetch_records()

def insert_records(data, **args):
    try:
        
        database = connect_database()

        if database:
            cursor = database.cursor()
            
            insert_query = f"INSERT INTO {args['name']} ({args['column_names']}) VALUES ({args['place_holders']})"
            data = [tuple(None if pd.isna(value) else value for value in row) for row in data.to_numpy()]

            cursor.executemany(insert_query, data)
            database.commit()

            if cursor.rowcount > 0:
                print(f"Successfully inserted {cursor.rowcount} records of {args['name']} data.")
            else:
                print(f"Failed to insert {args['name']} data.")
        
    except sql.Error as err:
        print(f"Database connection failed: {err}")
    finally:
        cursor.close()
        database.close()
    
    