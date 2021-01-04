import datetime
import os
import requests

from dotenv import load_dotenv
load_dotenv()

BITCOIN_API_URL = 'https://api.wazirx.com/api/v2/tickers'


def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL).json()
    btc_price_in_inr = response['btcinr']['last']
    btc_price_in_usd = response['btcusdt']['last']
    return {'inr': btc_price_in_inr, 'usd': btc_price_in_usd}


curr_prices = get_latest_bitcoin_price()
