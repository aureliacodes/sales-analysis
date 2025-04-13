import sqlite3
import pandas as pd
import matplotlib.pyplot as plt 

db_file = 'sales_data.db'

# Connect to the database 
conn = sqlite3.connect(db_file)
print(f"Connected to the database {db_file}.")

# --- Example 1: Data extraction using SQL and loading into Pandas ----
print("\n--- Extracting order and custumers ---")
# Scriem un query SQL pentru a combina informatii din mai multe tabele
query_orders_customers = """
SELECT
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    c.email,
    o.total_amount 
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
"""
# We use pandas.read_sql_query to execute the query and obtain a DataFrame.
df_orders = pd.read_sql_query(query_orders_customers, conn)
print("Datele comenzilor si clientilor extrase:")
print(df_orders.head()) # We display the first 5 rows.

# --- Example 2: Data Cleaning with Pandas ---
print("\n--- Data Cleaning ---")
# Checking for missing values
print("Missing values before cleaning:")
print(df_orders.isnull().sum())

# Convert the 'order_date' column to datetime format
df_orders['order_date'] = pd.to_datetime(df_orders['order_date'], errors='coerce') 
# errors='coerce' will convert invalid data to NaT (Not a Time)

# Fill missing values in 'total_amount' with 0 or with the mean/median (choosing 0 here)
# In a real project, we would investigate why values are missing (maybe recalculated from order_items)
initial_missing_count = df_orders['total_amount'].isnull().sum()
df_orders['total_amount'].fillna(0, inplace=True) 
print(f"\nReplaced {initial_missing_count} missing values in 'total_amount' with 0.")

# Check for missing values again
print("\nMissing values after cleaning:")
print(df_orders.isnull().sum())

# Display data types to verify date conversion
print("\nData types after cleaning:")
print(df_orders.dtypes)

# --- Example 3: Simple Analysis with Pandas ---
print("\n--- Data Analysis ---")
# 1. How many orders did each customer place?
customer_order_counts = df_orders['email'].value_counts()
print("\nNumber of orders per customer:")
print(customer_order_counts)


# 2. What is the total value of orders per customer?
customer_total_spent = df_orders.groupby(['email', 'first_name', 'last_name'])['total_amount'].sum().sort_values(ascending=False)
print("\nTotal amount spent per customer:")
print(customer_total_spent)

# 3. Total sales per month
# Extract month and year from the order date
df_orders['order_month'] = df_orders['order_date'].dt.to_period('M') 
monthly_sales = df_orders.groupby('order_month')['total_amount'].sum()
print("\nTotal sales per month:")
print(monthly_sales)

# --- Example 4: Analysis combining multiple tables (using SQL) ---
print("\n--- Top Sold Products ---")
query_top_products = """
SELECT
    p.product_name,
    SUM(oi.quantity) as total_quantity_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;
"""
df_top_products = pd.read_sql_query(query_top_products, conn)
print("Top sold products (by quantity):")
print(df_top_products)

# --- Example 5: Simple Visualization (Optional) ---
print("\n--- Monthly Sales Visualization ---")
# Ensure the index is a string for plotting
monthly_sales.index = monthly_sales.index.astype(str) 

plt.figure(figsize=(10, 5)) # Create a figure
monthly_sales.plot(kind='bar', title='Total Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales (RON)')
plt.xticks(rotation=45) # Rotate the labels on the X-axis
plt.tight_layout() # Adjust the layout
# plt.show() # Displays the interactive plot
plt.savefig('monthly_sales.png') # Save the plot as an image
print("Monthly sales chart saved as 'monthly_sales.png'.")

# Close connection
conn.close()
print("\nDatabase connection closed.")
