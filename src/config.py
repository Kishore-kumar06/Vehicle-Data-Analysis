# --- Database ---
DB_HOST     = "localhost"
DB_PORT     = 3306
DB_USER     = "root"
DB_PASSWORD = "kum@r1998"   # <-- change this
DB_NAME     = "vehicle_expense_db"
AUTH_PLUGIN = "mysql_native_password"

# --- Data ---
CLEANED_DATA_FOLDER = "data/cleaned"

# --- Upload order matters (FK dependencies) ---
TABLE_UPLOAD_ORDER = [
    "users",
    "vehicles",
    "locations",
    "products",
    "fuel_price_history",
    "transactions",
]
