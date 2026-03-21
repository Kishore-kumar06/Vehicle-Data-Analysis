import pandas as pd
from src.db_connection import get_connection


def upload_table(df, table_name):
    if df.empty:
        print(f"  Skipping {table_name} — dataframe is empty.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    # Check how many rows exist before inserting
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    rows_before = cursor.fetchone()[0]

    # Build the INSERT query dynamically from column names
    columns      = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    query        = f"INSERT IGNORE INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Convert dataframe rows to list of tuples
    # NaN -> None so MySQL stores NULL instead of the string "nan"
    rows = [
        tuple(None if pd.isna(val) else val for val in row)
        for row in df.itertuples(index=False, name=None)
    ]

    cursor.executemany(query, rows)
    connection.commit()

    # Check rows after insert
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    rows_after = cursor.fetchone()[0]

    inserted = rows_after - rows_before
    print(f"  {table_name}: {inserted} new rows inserted  (total in DB: {rows_after})")

    cursor.close()
    connection.close()
