from src.db_connection import get_connection


# SQL to create each table
CREATE_USERS = """
CREATE TABLE IF NOT EXISTS users (
    user_id   INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    email     VARCHAR(100),
    address   VARCHAR(100)
);
"""

CREATE_VEHICLES = """
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id    INT PRIMARY KEY,
    vehicle_model VARCHAR(100) NOT NULL,
    brand         VARCHAR(100),
    engine_cc     INT,
    purchase_date DATE
);
"""

CREATE_LOCATIONS = """
CREATE TABLE IF NOT EXISTS locations (
    location_id   INT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    address       VARCHAR(100),
    city          VARCHAR(50),
    state         VARCHAR(50),
    pin_code      int
);
"""

CREATE_PRODUCTS = """
CREATE TABLE IF NOT EXISTS products (
    product_id   INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category     VARCHAR(50),
    is_fuel      BIT,
    is_service   BIT
);
"""

CREATE_FUEL_PRICE_HISTORY = """
CREATE TABLE IF NOT EXISTS fuel_price_history (
    fuel_price_id    INT,
    fuel_price       DECIMAL(8, 2),
    price_trend_date DATE
);
"""

CREATE_TRANSACTIONS = """
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id   INT PRIMARY KEY,
    user_id          INT,
    vehicle_id       INT,
    location_id      INT,
    product_id       INT,
    price            DECIMAL(10, 2),
    quantity         DECIMAL(10, 2),
    total_cost       DECIMAL(10, 2),
    transaction_date DATE,
    FOREIGN KEY (user_id)     REFERENCES users(user_id),
    FOREIGN KEY (vehicle_id)  REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id),
    FOREIGN KEY (product_id)  REFERENCES products(product_id)
);
"""

ALL_TABLES = [
    ("users",              CREATE_USERS),
    ("vehicles",           CREATE_VEHICLES),
    ("locations",          CREATE_LOCATIONS),
    ("products",           CREATE_PRODUCTS),
    ("fuel_price_history", CREATE_FUEL_PRICE_HISTORY),
    ("transactions",       CREATE_TRANSACTIONS),
]


def create_all_tables():
    """Create all tables. Safe to run multiple times (IF NOT EXISTS)."""
    connection = get_connection()
    cursor = connection.cursor()

    for table_name, sql in ALL_TABLES:
        cursor.execute(sql)
        print(f"  Table ready: {table_name}")

    connection.commit()
    cursor.close()
    connection.close()
    print("All tables created successfully.")

