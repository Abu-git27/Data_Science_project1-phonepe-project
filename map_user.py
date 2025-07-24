import pandas as pd
import json
import os

# Folder path
path = "data/map/user/hover/country/india/state/"
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
    state_path = path + state + "/"
    if not os.path.isdir(state_path):
        continue

    year_list = os.listdir(state_path)

    for year in year_list:
        year_path = state_path + year + "/"
        if not os.path.isdir(year_path):
            continue

        quarter_list = os.listdir(year_path)

        for file in quarter_list:
            file_path = year_path + file
            with open(file_path, 'r') as f:
                data = json.load(f)

                if 'data' in data and 'hoverData' in data['data']:
                    state_data = data['data']['hoverData']
                    for district, value in state_data.items():
                        reg_users = value.get('registeredUsers', 0)
                        app_opens = value.get('appOpens', 0)

                        clm['State'].append(state)
                        clm['Year'].append(year)
                        clm['Quarter'].append(int(file.strip('.json')))
                        clm['RegisteredUsers'].append(reg_users)
                        clm['AppOpens'].append(app_opens)

# Create DataFrame
Map_User = pd.DataFrame(clm)
print(Map_User)
