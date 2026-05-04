'''
Description:-
Fetch weather data for multiple cities using Open-Meteo API and save it as CSV.
'''

import requests
import pandas as pd
from datetime import datetime
import numpy as np

cities = [
    {"name": "New York", "latitude": 40.7128, "longitude": -74.0060},
    {"name": "Bengaluru", "latitude": 12.9716, "longitude": 77.5946},
    {"name": "London", "latitude": 51.5074, "longitude": -0.1278},
    {"name": "Tokyo", "latitude": 35.6895, "longitude": 139.6917}
]

rows=[]

for c in cities:
    url ="https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": c["latitude"],
        "longitude": c["longitude"],
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    weather = data['current_weather']
    weather["city"] = c["name"]

    rows.append(weather)

df=pd.DataFrame(rows)
df['temp_category'] =np.where(df['temperature'] > 25, 'Hot', 'Not Hot')

df.to_csv("multiple_city_weather.csv",index=True)
print(df)