import os
import json
import pandas as pd

# ✅ Set correct base path
base_path = os.path.join('..', 'data', 'aggregated', 'user', 'country', 'india', 'state')

# ✅ Ensure path exists
if not os.path.exists(base_path):
    raise FileNotFoundError(f"Directory not found: {base_path}")

# ✅ Ensure output folder exists
os.makedirs('../csv_output', exist_ok=True)

# ✅ Initialize data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Brand': [],
    'RegisteredUsers': [],
    'AppOpens': []
}

# ✅ Loop through all states, years, and quarters
for state in os.listdir(base_path):
    state_path = os.path.join(base_path, state)
    if not os.path.isdir(state_path): continue

    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        if not os.path.isdir(year_path): continue

        for file in os.listdir(year_path):
            if not file.endswith('.json'): continue
            file_path = os.path.join(year_path, file)

            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    devices = data.get('data', {}).get('usersByDevice', [])
                    if not isinstance(devices, list):
                        continue
                except json.JSONDecodeError:
                    continue

            for device in devices:
                clm['State'].append(state.replace('-', ' ').title())
                clm['Year'].append(int(year))
                clm['Quarter'].append(int(file.strip('.json')))
                clm['Brand'].append(device.get('brand', 'Unknown'))
                clm['RegisteredUsers'].append(device.get('count', 0))
                clm['AppOpens'].append(device.get('percentage', 0))

# ✅ Convert to DataFrame
df = pd.DataFrame(clm)
print(df.head())

# ✅ Save to CSV
df.to_csv('../csv_output/agg_user_by_device.csv', index=False)
