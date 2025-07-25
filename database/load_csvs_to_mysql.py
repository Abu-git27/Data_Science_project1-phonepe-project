import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os

# MySQL connection details
username = 'root'
password = '12345'  # 🔁 Replace with your actual MySQL password
host = 'localhost'
port = 3306
database = 'phonepe_data'

# Create SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Folder containing CSVs
csv_folder = 'csv_output'

# List of CSV filenames
csv_files = {
    'agg_insurance': 'agg_insurance.csv',
    'agg_transaction': 'agg_transaction.csv',
    'agg_user': 'agg_user.csv',
    'map_insurance': 'map_insurance.csv',
    'map_transaction': 'map_transaction.csv',
    'map_user': 'map_user.csv',
    'top_insurance': 'top_insurance.csv',
    'top_transaction': 'top_transaction.csv',
    'top_user': 'top_user.csv',
}

# Load each CSV into MySQL
for table_name, filename in csv_files.items():
    csv_path = os.path.join(csv_folder, filename)
    if os.path.exists(csv_path):
        print(f"📥 Loading {filename} into table `{table_name}`...")
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"✅ Successfully loaded: {table_name}")
    else:
        print(f"❌ File not found: {filename}")
