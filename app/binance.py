import json
from urllib.request import urlopen
from typing import List

BASE_URL = "https://api.binance.com/api/v3"

def get_klines(symbol: str, interval: str, limit: int = 100) -> List[float]:
    """Fetch closing prices from Binance public API."""
    url = f"{BASE_URL}/klines?symbol={symbol}&interval={interval}&limit={limit}"
    with urlopen(url) as resp:
        data = json.load(resp)
    return [float(item[4]) for item in data]
