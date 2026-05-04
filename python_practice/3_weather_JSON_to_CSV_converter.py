'''
Fetch live API data , save raw JSON and convert to CSV using Pandas and NumPy.
'''

import requests
import pandas as pd
import numpy as np
import json

from tomlkit import date

url="https://api.open-meteo.com/v1/forecast"

params={
    'latitude': 40.7128,
    'longitude': -74.0060,
    'hourly': "temperature_2m"
}

response = requests.get(url, params=params)
data=response.json()

with open("weather_data.json", "w") as file:
    json.dump(data, file, indent=4)

#print(data)
df=pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})

df["temperature_f"] = df["temperature"] * 9/5 + 32

df.to_csv("weather_data_hourly.csv", index=False)

print(df.head())