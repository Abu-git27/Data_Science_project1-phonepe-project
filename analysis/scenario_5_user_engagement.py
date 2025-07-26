import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn theme
sns.set(style="whitegrid")

# Define CSV paths
map_user_path = os.path.join('..', 'csv_output', 'map_user.csv')
top_user_path = os.path.join('..', 'csv_output', 'top_user.csv')

# Load data
map_df = pd.read_csv(map_user_path)
top_df = pd.read_csv(top_user_path)

# Print column names for reference
print("Map User Columns:", map_df.columns)
print("Top User Columns:", top_df.columns)

# ----------------- 🔹 Top 10 Districts by Registered Users -----------------
top_districts = map_df.groupby('District')['RegisteredUsers'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_districts.values, y=top_districts.index, palette='viridis')
plt.title('Top 10 Districts by Registered Users')
plt.xlabel('Total Registered Users')
plt.ylabel('District')
plt.tight_layout()
plt.show()

# ----------------- 🔹 Top 10 Districts by App Opens -----------------
top_app_opens = map_df.groupby('District')['AppOpens'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_app_opens.values, y=top_app_opens.index, palette='rocket')
plt.title('Top 10 Districts by App Opens')
plt.xlabel('Total App Opens')
plt.ylabel('District')
plt.tight_layout()
plt.show()

# ----------------- 🔹 App Opens vs Registered Users (Engagement Ratio) -----------------
plt.figure(figsize=(12, 6))
sns.scatterplot(data=map_df, x='RegisteredUsers', y='AppOpens', hue='State', alpha=0.7)

plt.title('App Opens vs Registered Users (Engagement Ratio)')
plt.xlabel('Registered Users')
plt.ylabel('App Opens')
plt.grid(True)

# Place legend outside the chart area (right side)
plt.legend(
    title='State',
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    borderaxespad=0.,
    fontsize='small'
)

plt.tight_layout()
plt.show()
