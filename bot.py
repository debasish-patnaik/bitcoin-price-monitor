import datetime
import os
import requests

from dotenv import load_dotenv
load_dotenv()

BITCOIN_API_URL = 'https://api.wazirx.com/api/v2/tickers'
IFTTT_URL = 'https://maker.ifttt.com/trigger/bitcoin_alert/with/key/'


def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL).json()
    btc_price_in_inr = response['btcinr']['last']
    btc_price_in_usd = response['btcusdt']['last']
    return {'inr': btc_price_in_inr, 'usd': btc_price_in_usd}


curr_prices = get_latest_bitcoin_price()

curr_time = datetime.datetime.now().strftime('%d-%b-%Y %I:%M %p')


print(requests.post(IFTTT_URL + os.getenv('ifttt_api_key'),
                    data={'value1': curr_time, 'value2': curr_prices['inr'], 'value3': curr_prices['usd']}).content.decode('ascii'))
