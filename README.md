# Vehicle Expense Analytics

A personal project to track and analyse 5+ years of bike expenses using Python, MySQL, and Power BI.

## What it does

Loads cleaned expense data (fuel, maintenance, accessories) into a MySQL database and generates an interactive Power BI dashboard for analysis.

## Tech Stack

| Tool       | Purpose                        |
|------------|--------------------------------|
| Python     | Data cleaning & DB upload      |
| pandas     | Reading and cleaning CSV files |
| MySQL      | Storing the data               |
| Power BI   | Dashboard and visualisation    |

## Project Structure

```
vehicle-analysis/
├── data/
│   └── cleaned/          # cleaned CSV files (6 tables)
├── src/
│   ├── config.py         # DB credentials and settings
│   ├── db_connection.py  # MySQL connection helper
│   ├── create_tables.py  # CREATE TABLE statements
│   ├── data_cleaner.py   # pandas cleaning functions
│   ├── data_uploader.py  # inserts data into MySQL
│   └── db_verifier.py    # post-upload checks
├── main.py               # run this to execute the pipeline
├── requirements.txt
└── README.md
```

## Database Schema

6 tables with foreign key relationships:

```
users ──────────────────────┐
vehicles ───────────────────┤
locations ──────────────────┼──► transactions
products ───────────────────┘
fuel_price_history (standalone)
```

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create the MySQL database:
   ```sql
   CREATE DATABASE vehicle_expense_db;
   ```

3. Update your credentials in `src/config.py`

4. Run the pipeline:
   ```bash
   python main.py
   ```

## Sample Output

```
Step 1: Creating tables...
  Table ready: users
  Table ready: vehicles
  ...

Step 2: Loading cleaned CSV files...
  Loaded: transactions (200 rows)
  ...

Step 3: Uploading data to MySQL...
  transactions: 200 new rows inserted (total in DB: 200)
  ...

Step 4: Verifying upload...
  transactions          200 rows   [OK]
  Total spend: Rs. 1,48,276.00
  Total fuel:  Rs. 61,785.00
```

## Key Findings

- Total spend over 5 years: **₹1,48,276**
- Fuel cost: ₹61,785 (41.7%) — Maintenance: ₹86,491 (58.3%)
- Petrol prices rose from ₹83 (2020) to ₹113 (2021 peak)
- Actual mileage: 35.8 km/L vs ARAI rated 40 km/L
- 99% of fuel purchases at a single station (Bharath Petroleum, Bangalore)
