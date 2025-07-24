import pandas as pd
import json
import os

# Folder path
path = "data/map/insurance/country/india/state/"
state_list = os.listdir(path)

# Dictionary to store extracted data
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'InsuranceCount': [],
    'SumAssured': []  # Placeholder, data doesn't have this field but kept for consistency
}

# Loop through all states, years, and quarters
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

                if 'data' in data and 'data' in data['data'] and 'data' in data['data']['data']:
                    for entry in data['data']['data']['data']:
                        district = entry[3]
                        insurance_count = entry[2]

                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['District'].append(district)
                        clm['InsuranceCount'].append(insurance_count)
                        clm['SumAssured'].append(None)  # Not available in this dataset

# Create DataFrame
Map_Insurance = pd.DataFrame(clm)
print(Map_Insurance)
