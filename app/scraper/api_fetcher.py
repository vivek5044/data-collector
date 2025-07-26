import requests
from ..config import FINNHUB_API_KEY

def get_stock_price(symbol):
    # Adjust symbol format depending on API provider
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    res = requests.get(url)
    return res.json()
