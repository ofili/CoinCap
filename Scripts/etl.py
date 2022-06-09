# Import libraries
import os
import sys
import requests
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt


# Settings
base_path = os.path.abspath("__file__" + "/../")
print(base_path)


# Variables for CoinCap data
url = "https://api.coincap.io/v2/assets"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
payload = {'limit': '100'}

# Get CoinCap data
def get_coin_cap_data():
    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    return data

json_data = get_coin_cap_data()
df = pd.read_json(json_data)
df.to_csv('coin_cap_data.csv', index=False)



