# Sales Data Analysis (Python & SQL)

## Overview
This project uses Python and SQLite for analyzing sales data. It loads data from CSV files into a relational database, extracts insights such as top-performing products and customers, and generates optional visualizations using Matplotlib and Seaborn.

## Features
- Data loading and preprocessing with Pandas.
- SQL queries to analyze sales metrics (e.g., revenue, customer behavior, product trends).
- Optional data visualization with Matplotlib and Seaborn.
- Modular structure for easy setup and execution.

## Technologies Used
- **Python 3.x** – scripting and data manipulation.
- **SQLite** – lightweight relational database.
- **Pandas** – for working with tabular data.
- **Matplotlib & Seaborn** – for creating plots (optional).

## Project Structure
```
python-sql-sales-analysis/
├── data/                # Raw CSV files and SQLite database
│   ├── products.csv
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── sales_data.db
├── scripts/             # Python scripts for database setup and analysis
│   ├── database_setup.py
│   └── sales_analysis.ipynb
├── visualizations/      # Generated plots
│   └── monthly_sales.png
├── README.md            # Project documentation
├── .gitignore           # Files excluded from version control
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/aureliacodes/sales-analysis.git
cd sales-analysis
```

### 2. (Optional) Create a Virtual Environment
```bash
python -m venv venv
# Activate:
# Windows: .\venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas matplotlib seaborn
```

### 4. Set Up the Database
```bash
python scripts/database_setup.py
```

### 5. Run the Analysis
```bash
jupyter notebook scripts/sales_analysis.ipynb
```

## License
This project is for educational purposes. Feel free to fork or adapt it.
