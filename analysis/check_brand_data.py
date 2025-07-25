import json
import os

file_path = 'data/aggregated/user/country/india/state/andhra-pradesh/2018/1.json'

with open(file_path, 'r') as f:
    data = json.load(f)

if 'usersByDevice' in data.get('data', {}):
    print("✅ Brand-wise data is present.")
    print("Sample:", data['data']['usersByDevice'][:2])  # print 2 brands
else:
    print("❌ Brand-wise data not found.")
