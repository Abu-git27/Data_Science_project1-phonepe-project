import pandas as pd
import json
import os

# Folder path
path = 'data/top/transaction/country/india/state/'

# Create output folder if it doesn't exist
os.makedirs('csv_output', exist_ok=True)

# Dictionary to store extracted data
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Pincode': [],
    'Transaction_count': [],
    'Transaction_amount': []
}

# Loop through all states, years, and quarters
state_list = os.listdir(path)

for state in state_list:
    state_path = os.path.join(path, state)
    year_list = os.listdir(state_path)

    for year in year_list:
        year_path = os.path.join(state_path, year)
        file_list = os.listdir(year_path)

        for file in file_list:
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)

            if 'data' in data and 'pincodes' in data['data']:
                for record in data['data']['pincodes']:
                    clm['State'].append(state)
                    clm['Year'].append(year)
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['Pincode'].append(record['entityName'])
                    clm['Transaction_count'].append(record['metric']['count'])
                    clm['Transaction_amount'].append(record['metric']['amount'])

# Create DataFrame
Top_Transaction = pd.DataFrame(clm)
print(Top_Transaction)
Top_Transaction.to_csv('csv_output/top_transaction.csv', index=False)
