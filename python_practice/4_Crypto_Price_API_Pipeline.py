'''
Fetch live crypto prices from coinGecko and save them into CSV file.

'''


import requests
import pandas as pd
from datetime import datetime
import numpy as np 


url="https://api.coingecko.com/api/v3/simple/price"

params={
    'ids': 'bitcoin,ethereum',
    'vs_currencies': 'usd'
}
data = requests.get(url, params=params).json()

print(data)

rows = []

for coin,price in data.items():
    rows.append({
        "coin": coin,
        "price_usd": price['usd'],
        "extracted_at": datetime.now()
    })

print(rows)

df=pd.DataFrame(rows)

df['price_category'] = np.where(df['price_usd'] > 20000, 'Expensive', 'Affordable')
df.to_csv("crypto_price.csv", index=False)