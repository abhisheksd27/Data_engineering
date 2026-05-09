#Fetch hourly weather and aggregate it into daily metrics

import requests
import pandas as pd
import numpy as np

url ="https://api.open-meteo.com/v1/forecast"

param={
    'latitude':40.7128,
    'longitude':-74.0060,
    'hourly':'temperature_2m,relative_humidity_2m',
}

data = requests.get(url, params=param).json()

"""df=pd.DataFrame(data)
print(df)"""

df=pd.DataFrame({
    "time":data['hourly']['time'],
    "temperature":data['hourly']['temperature_2m'],
})

daily=df.groupby("date").agg