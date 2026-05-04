'''Description

Fetch live weather data from Open-Meteo API and save it as CSV.

Steps
Connect to weather API
Extract JSON data
Convert to Pandas DataFrame
Add NumPy calculated column
Save CSV file '''

import requests 
import pandas as pd
import numpy as np
from datetime import datetime

url="https://api.open-meteo.com/v1/forecast"
params={
    'latitude': 40.7128,
    'longitude': -74.0060,
    'current_weather': True
}

response = requests.get(url, params=params)
#print(response.status_code)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['current_weather']
    #print(weather)
    df=pd.DataFrame([weather])
    df['city'] ="Bengaluru"
    df['extracted_at'] = datetime.now()
    df['temp_f'] = df['temperature'] * 9/5 + 32
    df.to_csv('weather_data.csv', index=False)
    print("Data saved to weather_data.csv")
else:
    print(f"Failed to fetch data: {response.status_code}")
