import sqlite3
import pandas as pd

# The names of the CSV files and the database
db_file = 'sales_data.db'
csv_files = {
    'products': 'products.csv',
    'customers': 'customers.csv',
    'orders': 'orders.csv',
    'order_items': 'order_items.csv'
}
# Connect to the database (it will be created if it doesn't exist)
# The database file will be created in the same directory as this script

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
print(f"Baza de date {db_file} creata/conectata.")

# --- Create tables ---
# Products
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL
)
''')
print("Tabel 'products' creat (daca nu exista).")

# Customers
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE
)
''')
print("Tabel 'customers' creat (daca nu exista).")

# Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    total_amount REAL, 
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
)
''')
print("Tabel 'orders' creat (daca nu exista).")

# Order Items
cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders (order_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
)
''')
print("Tabel 'order_items' creat (daca nu exista).")

# Loop through the CSV files and load them into the corresponding tables
for table_name, csv_file in csv_files.items():
    try:
        df = pd.read_csv(csv_file)
        # We use to_sql to insert the data from the DataFrame into the SQL table
        # if_exists='replace' will delete the table and recreate it – useful at the beginning
        # if_exists='append' would add data if the table already exists
        # For the first run, 'replace' is fine. For later runs, you might want 'append' or custom logic.
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"The data from {csv_file} has been loaded into table {table_name}.")
    except FileNotFoundError:
        print(f"ERROR: The file {csv_file} was not found.")
    except Exception as e:
        print(f"ERROR loading {csv_file}: {e}")

# Save (commit) and close the connection
conn.commit()
conn.close()

print(f"Data saved. Connection to {db_file} closed.")
# Note: This script assumes that the CSV files are in the same directory as this script.