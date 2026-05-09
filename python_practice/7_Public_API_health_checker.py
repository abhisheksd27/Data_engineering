#check wether multiple public APIs are healthy or not


import requests
import pandas as pd
import numpy as np

apis=[
    "https://api.github.com",
    "https://api.openweathermap.org",
    "https://jsonplaceholder.typicode.com"

]

rows=[]

for api in apis:
    try:
        res=requests.get(api,timeout=5 )
        rows.append(
            {
                "api_url":api,
                "status_code":res.status_code,
                'response_time':res.elapsed.total_seconds()
            } 
        )
    except requests.exceptions.RequestException as e:
        rows.append(
            {
                "api_url":api,
                "status_code":None,
                'response_time':None
               
            }
        )
        print(f"Error checking {api}: {e}")

df=pd.DataFrame(rows)
df["status"] = np.where(df["status_code"]==200, "Healthy", "Unhealthy")

df.to_csv("api_health_status.csv", index=False)

print(df)