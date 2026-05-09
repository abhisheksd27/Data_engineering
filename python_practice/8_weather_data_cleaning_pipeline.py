#extract weather data and clean missing / invalid values

import requests
import pandas as pd
import numpy as np

url="https://api.open-meteo.com/v1/forecast"
param={
    'latitude':40.7128,
    'longitude':-74.0060,
    'hourly':'temperature_2m,relative_humidity_2m',
}

data = requests.get(url, params=param).json()

df=pd.DataFrame(
    {
        'time':data['hourly']['time'],
        'temperature':data['hourly']['temperature_2m'],
        'humidity':data['hourly']['relative_humidity_2m']
    }
)

df["temperature"]=df["temperature"].fillna(df['temperature'].mean())
df["humidity"]=df["humidity"].fillna(df['humidity'].median())

df["comfort_index"]=np.round(df["temperature"]- (df['humidity']/100),2)
df.to_csv("clean_weather.csv",index=False)

print(df.head())