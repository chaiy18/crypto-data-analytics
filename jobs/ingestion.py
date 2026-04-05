import requests
import pandas as pd
from datetime import datetime

def run():
    print("Running ingestion...")

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    rows = []
    for coin, value in data.items():
        rows.append({
            "coin": coin,
            "price": value["usd"],
            "timestamp": datetime.now()
        })

    df = pd.DataFrame(rows)

    path = f"data/raw/crypto_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
    df.to_csv(path, index=False)

    print(f"Saved raw data → {path}")
    return path