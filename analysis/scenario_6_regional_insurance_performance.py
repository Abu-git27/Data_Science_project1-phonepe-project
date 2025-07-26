import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn theme
sns.set(style="whitegrid")

# Define CSV paths
map_insurance_path = os.path.join('..', 'csv_output', 'map_insurance.csv')

# Load data
map_df = pd.read_csv(map_insurance_path)

# Print column names for verification
print("Columns in map_insurance.csv:", map_df.columns)

# Remove unknown districts
map_df = map_df[map_df['District'].str.lower() != 'unknown']

# ----------------- 🔹 Top 10 Districts by Insurance Count -----------------
top_districts = map_df.groupby('District')['InsuranceCount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_districts.values, y=top_districts.index, palette='viridis')
plt.title('Top 10 Districts by Insurance Count', fontsize=14)
plt.xlabel('Total Insurance Count')
plt.ylabel('District')
plt.tight_layout()
plt.savefig('../plots/top10_districts_insurance_count.png')
plt.show()

# ----------------- 🔹 Top 10 States by Insurance Count -----------------
top_states = map_df.groupby('State')['InsuranceCount'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_states.values, y=top_states.index, palette='magma')
plt.title('Top 10 States by Insurance Count', fontsize=14)
plt.xlabel('Total Insurance Count')
plt.ylabel('State')
plt.tight_layout()
plt.savefig('../plots/top10_states_insurance_count.png')
plt.show()

# ----------------- 🔹 Quarterly Trend Plot -----------------
quarterly_trend = map_df.groupby(['Year', 'Quarter'])['InsuranceCount'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=quarterly_trend, x='Quarter', y='InsuranceCount', hue='Year', marker='o', palette='tab10')
plt.title('Quarterly Insurance Count Trend (Year-wise)', fontsize=14)
plt.xlabel('Quarter')
plt.ylabel('Total Insurance Count')
plt.xticks([1, 2, 3, 4])
plt.tight_layout()
plt.savefig('../plots/quarterly_insurance_trend.png')
plt.show()

# ----------------- 🔹 District-wise Insurance Spread (Clean Scatter Plot) -----------------
# Aggregate and sort districts by total insurance count
district_totals = map_df.groupby(['State', 'District'])['InsuranceCount'].sum().reset_index()
top_districts = district_totals.sort_values(by='InsuranceCount', ascending=False).head(30)

plt.figure(figsize=(14, 8))
sns.stripplot(data=top_districts, x='InsuranceCount', y='District', hue='State', palette='Set2', size=8, jitter=True, alpha=0.8)
plt.title('District-wise Insurance Spread by State (Top 30)', fontsize=14)
plt.xlabel('Insurance Count')
plt.ylabel('District')
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout()
plt.savefig('../plots/district_insurance_spread_top30.png')
plt.show()

print("✅ Scenario 6: All visualizations completed and exported to '../plots/' folder.")
