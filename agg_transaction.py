import pandas as pd
import json
import os

# Path to aggregated transaction data
path = "data/aggregated/transaction/country/india/state/"
state_list = os.listdir(path)

clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Transaction_type': [],
    'Transaction_count': [],
    'Transaction_amount': []
}

for state in state_list:
    state_path = path + state + "/"
    year_list = os.listdir(state_path)

    for year in year_list:
        year_path = state_path + year + "/"
        file_list = os.listdir(year_path)

        for file in file_list:
            file_path = year_path + file
            with open(file_path, 'r') as f:
                data = json.load(f)

                if 'data' in data and 'transactionData' in data['data']:
                    for record in data['data']['transactionData']:
                        t_type = record['name']
                        count = record['paymentInstruments'][0]['count']
                        amount = record['paymentInstruments'][0]['amount']

                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['Transaction_type'].append(t_type)
                        clm['Transaction_count'].append(count)
                        clm['Transaction_amount'].append(amount)

Agg_Transaction = pd.DataFrame(clm)
print(Agg_Transaction)
