# Vehicle Expense Analytics

End-to-end personal vehicle expense analytics system—from raw Excel data to interactive Power BI dashboard. Tracks 5+ years of bike expenses (Aug 2020 – Dec 2025) for a TVS NTorq 125 that describes the expenses that occurred for the vehicle during the provided period.


## Course of Action

Recorded each transaction, such as fuel, maintenance, accessories, and further metrics, in the Excel sheet in a raw format, each per date. Further transformed the raw data by normalizing the columns and creating a data model using a star schema and by using Python (Pandas and mysql.connector libraries) that loads cleaned expense data (fuel, maintenance, and accessories) into a MySQL database and generates an interactive Power BI dashboard for analysis.

## Tech Stack

| Tool       | Purpose                        |
|------------|--------------------------------|
| Python     | Data cleaning & DB upload      |
| Pandas     | Reading and cleaning CSV files |
| MySQL      | Storing the data               |
| Power BI   | Dashboard and visualisation    |
| Excel      | Tracking Data                  |

## Project Structure

```
vehicle-analysis/
├── data/
│   └── cleaned/ # cleaned CSV files (6 tables)
├── powerbi/
|   └── latest_dashboard/
|       └── screenshots/
|   ├── vehicle_expenses_analytics.pbix
|   └── old_dashboard/
|       └── screenshots/
|    ├── bike_analytics.pbix
├── src/
│   ├── db_config.py      # DB credentials and settings
│   ├── db_connection.py  # MySQL connection helper
│   ├── create_tables.py  # CREATE TABLE statements
│   ├── data_cleaner.py   # pandas cleaning functions
│   ├── data_uploader.py  # inserts data into MySQL
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

3. Update the credentials in `src/config.py`

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

## PowerBi Dashboard Pages

Page 1 — Executive Overview
Page 2 — Fuel Analysis
Page 3 — Maintenance & Service
Page 4 — Location Insights
Page 5 — Year-on-Year

## Key Findings

- Total spend over 5 years: **₹82,691**
- Fuel cost: ₹58,985 — Maintenance: ₹23,706
- Petrol prices rose from ₹83 (2020) to ₹113 (2021 peak)
- Actual mileage: 35.8 km/L vs ARAI rated 45.5 km/L
- 99% of fuel purchases at a single station (Bharath Petroleum, Bangalore)


## Note: 
- Power BI Dashboards are under upgradation.
