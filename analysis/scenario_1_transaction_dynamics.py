import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the aggregated transaction data
file_path = os.path.join('..', 'csv_output', 'agg_transaction.csv')
df = pd.read_csv(file_path)

# Convert Quarter to string format for labeling (e.g., '2020-Q1')
df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)

# Group by State and Year-Quarter to see trend
grouped = df.groupby(['State', 'YearQuarter']).agg({
    'Transaction_count': 'sum',
    'Transaction_amount': 'sum'
}).reset_index()

# ------------------ 🔹 Visualization 1: Transaction Count ------------------

plt.figure(figsize=(15, 8))
top_states = df.groupby('State')['Transaction_count'].sum().sort_values(ascending=False).head(5).index

for state in top_states:
    state_data = grouped[grouped['State'] == state]
    plt.plot(state_data['YearQuarter'], state_data['Transaction_count'], label=state)

plt.title('Top 5 States by Transaction Count Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Transaction Count')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()

# ------------------ 🔹 Visualization 2: Transaction Amount ------------------

plt.figure(figsize=(15, 8))

for state in top_states:
    state_data = grouped[grouped['State'] == state]
    plt.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)

plt.title('Top 5 States by Transaction Amount Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Transaction Amount (INR)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
