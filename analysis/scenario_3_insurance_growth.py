import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the aggregated insurance data
file_path = os.path.join('..', 'csv_output', 'agg_insurance.csv')
df = pd.read_csv(file_path)

# Create a combined Year-Quarter column for time series analysis
df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)

# Group by State and Year-Quarter
grouped = df.groupby(['State', 'YearQuarter']).agg({
    'Transaction_count': 'sum',
    'Transaction_amount': 'sum'
}).reset_index()

# Get Top 5 states with highest total insurance amount
top_states = grouped.groupby('State')['Transaction_amount'].sum().sort_values(ascending=False).head(5).index

# Plot: Insurance Transaction Count over Time
plt.figure(figsize=(14, 6))
for state in top_states:
    state_data = grouped[grouped['State'] == state]
    plt.plot(state_data['YearQuarter'], state_data['Transaction_count'], label=state)

plt.title('Top 5 States by Insurance Transaction Count Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Transaction Count')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot: Insurance Transaction Amount over Time
plt.figure(figsize=(14, 6))
for state in top_states:
    state_data = grouped[grouped['State'] == state]
    plt.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)

plt.title('Top 5 States by Insurance Transaction Amount Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Transaction Amount (INR)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
