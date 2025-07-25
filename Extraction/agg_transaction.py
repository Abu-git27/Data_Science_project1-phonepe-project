import pandas as pd
import json
import os

# Folder path
path = 'data/aggregated/transaction/country/india/state/'
os.makedirs('csv_output', exist_ok=True)

state_list = os.listdir(path)
clm = {
    'State': [], 'Year': [], 'Quarter': [],
    'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []
}

for state in state_list:
    state_path = os.path.join(path, state)
    for year in os.listdir(state_path):
        year_path = os.path.join(state_path, year)
        for file in os.listdir(year_path):
            file_path = os.path.join(year_path, file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                if 'data' in data and 'transactionData' in data['data']:
                    for record in data['data']['transactionData']:
                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['Transaction_type'].append(record['name'])
                        clm['Transaction_count'].append(record['paymentInstruments'][0]['count'])
                        clm['Transaction_amount'].append(record['paymentInstruments'][0]['amount'])

Agg_Transaction = pd.DataFrame(clm)
print(Agg_Transaction)
Agg_Transaction.to_csv('csv_output/agg_transaction.csv', index=False)
