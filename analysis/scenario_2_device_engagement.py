import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the device-wise user data
file_path = os.path.join('..', 'csv_output', 'agg_user_by_device.csv')
df = pd.read_csv(file_path)

# Create a combined 'Year-Quarter' column
df['YearQuarter'] = df['Year'].astype(str) + '-Q' + df['Quarter'].astype(str)

# Get top 5 brands by total registered users
top_brands = df.groupby('Brand')['RegisteredUsers'].sum().sort_values(ascending=False).head(5).index
filtered_df = df[df['Brand'].isin(top_brands)]

# ------------------ 🔹 Visualization 1: Registered Users Over Time ------------------

plt.figure(figsize=(14, 7))
for brand in top_brands:
    brand_data = filtered_df[filtered_df['Brand'] == brand]
    grouped = brand_data.groupby('YearQuarter')['RegisteredUsers'].sum().reset_index()
    plt.plot(grouped['YearQuarter'], grouped['RegisteredUsers'], label=brand)

plt.title('Top 5 Device Brands by Registered Users Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Registered Users')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------ 🔹 Visualization 2: AppOpens Percentage ------------------

plt.figure(figsize=(14, 7))
for brand in top_brands:
    brand_data = filtered_df[filtered_df['Brand'] == brand]
    grouped = brand_data.groupby('YearQuarter')['AppOpens'].mean().reset_index()
    plt.plot(grouped['YearQuarter'], grouped['AppOpens'], label=brand)

plt.title('Average App Opens % by Top 5 Brands Over Time')
plt.xlabel('Year-Quarter')
plt.ylabel('Average App Opens (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
