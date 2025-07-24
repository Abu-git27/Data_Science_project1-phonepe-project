import pandas as pd
import json
import os

# Folder path
path = "data/map/transaction/hover/country/india/"
year_list = os.listdir(path)

# Dictionary to store extracted data
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Transaction_count': [],
    'Transaction_amount': []
}

# Loop through all years and quarters
for year in year_list:
    year_path = os.path.join(path, year)
    if not os.path.isdir(year_path):
        continue

    file_list = os.listdir(year_path)

    for file in file_list:
        if not file.endswith(".json"):
            continue  # skip folders

        file_path = os.path.join(year_path, file)
        with open(file_path, 'r') as f:
            data = json.load(f)

            if 'data' in data and 'hoverDataList' in data['data']:
                for record in data['data']['hoverDataList']:
                    state = record['name']
                    count = record['metric'][0]['count']
                    amount = record['metric'][0]['amount']

                    clm['State'].append(state)
                    clm['Year'].append(year)
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['Transaction_count'].append(count)
                    clm['Transaction_amount'].append(amount)

# Create DataFrame
Map_Transaction = pd.DataFrame(clm)
print(Map_Transaction)
