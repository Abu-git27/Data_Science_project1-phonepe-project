import pandas as pd
import json
import os

# Folder path
path = "data/aggregated/user/country/india/state/"
state_list = os.listdir(path)

# Dictionary to store extracted data
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'RegisteredUsers': [],
    'AppOpens': []
}

# Loop through all states, years, and quarters
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

                if 'data' in data and 'aggregated' in data['data']:
                    agg_data = data['data']['aggregated']
                    registered_users = agg_data.get('registeredUsers')
                    app_opens = agg_data.get('appOpens')

                    clm['State'].append(state)
                    clm['Year'].append(year)
                    clm['Quarter'].append(int(file.strip('.json')))
                    clm['RegisteredUsers'].append(registered_users)
                    clm['AppOpens'].append(app_opens)

# Create DataFrame
Agg_User = pd.DataFrame(clm)
print(Agg_User)
