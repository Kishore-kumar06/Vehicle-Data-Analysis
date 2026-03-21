"""
main.py
-------
Run this file to execute the full pipeline:
  Step 1 - Create database tables
  Step 2 - Load and clean the CSV files
  Step 3 - Upload data to MySQL
  Step 4 - Verify the upload

Usage:
    python main.py
"""

from src.config import CLEANED_DATA_FOLDER, TABLE_UPLOAD_ORDER
from src.create_tables import create_all_tables
from src.data_cleaner import load_all_tables
from src.data_uploader import upload_table


def main():
    print("=" * 45)
    print("  Vehicle Expense Analytics — Pipeline")
    print("=" * 45)

    # Step 1: Create tables
    print("\nStep 1: Creating tables...")
    create_all_tables()

    # Step 2: Load and clean CSVs
    print("\nStep 2: Loading cleaned CSV files...")
    tables = load_all_tables(CLEANED_DATA_FOLDER)

    # Step 3: Upload in FK-safe order
    print("\nStep 3: Uploading data to MySQL...")
    for table_name in TABLE_UPLOAD_ORDER:
        if table_name in tables:
            upload_table(tables[table_name], table_name)
        else:
            print(f"  Warning: No CSV found for '{table_name}', skipping.")

    print("\nDone!")


if __name__ == "__main__":
    main()
