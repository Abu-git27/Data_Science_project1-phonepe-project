import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load required CSVs
agg_df = pd.read_csv(os.path.join('..', 'csv_output', 'agg_transaction.csv'))
map_df = pd.read_csv(os.path.join('..', 'csv_output', 'map_transaction.csv'))
top_df = pd.read_csv(os.path.join('..', 'csv_output', 'top_transaction.csv'))

# 🟦 Analyze: Top 10 states by total transaction amount
top_states = agg_df.groupby('State')['Transaction_amount'].sum().sort_values(ascending=False).head(10)
print("🔹 Top 10 States by Total Transaction Amount:\n", top_states)

# 📊 Plot 1: Bar chart for Top 10 states by Transaction Amount
plt.figure(figsize=(12, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='viridis')
plt.title('Top 10 States by Total Transaction Amount')
plt.xlabel('Transaction Amount (INR)')
plt.ylabel('State')
plt.tight_layout()
plt.grid(True)
plt.show()

# 🟨 Analyze: District-level high performers
top_districts = map_df.groupby('District')['TransactionAmount'].sum().sort_values(ascending=False).head(10)
print("🔸 Top 10 Districts by Transaction Amount:\n", top_districts)

# 📊 Plot 2: Bar chart for top 10 districts
plt.figure(figsize=(12, 6))
sns.barplot(x=top_districts.values, y=top_districts.index, palette='magma')
plt.title('Top 10 Districts by Transaction Amount')
plt.xlabel('Transaction Amount (INR)')
plt.ylabel('District')
plt.tight_layout()
plt.grid(True)
plt.show()

# 🟥 Analyze: Quarter-wise growth trend for top 3 states
top_3_states = top_states.head(3).index
agg_df['YearQuarter'] = agg_df['Year'].astype(str) + '-Q' + agg_df['Quarter'].astype(str)

plt.figure(figsize=(14, 6))
for state in top_3_states:
    state_data = agg_df[agg_df['State'] == state]
    plt.plot(state_data['YearQuarter'], state_data['Transaction_amount'], label=state)

plt.title('Quarterly Transaction Amount Trend (Top 3 States)')
plt.xlabel('Year-Quarter')
plt.ylabel('Transaction Amount')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
