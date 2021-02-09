import datetime
import os
import requests

from dotenv import load_dotenv
load_dotenv()

BITCOIN_API_URL = 'https://api.wazirx.com/api/v2/tickers'
IFTTT_URL = 'https://maker.ifttt.com/trigger/bitcoin_alert/with/key/'

eth_price_in_inr = ''


def get_latest_crypto_prices():
    global eth_price_in_inr
    response = requests.get(BITCOIN_API_URL).json()
    btc_price_in_inr = response['btcinr']['last']
    btc_price_in_usd = response['btcusdt']['last']
    eth_price_in_inr = response['ethinr']['last']
    return {'inr': btc_price_in_inr, 'usd': btc_price_in_usd}


istTimeDelta = datetime.timedelta(hours=5, minutes=30)
istTZObject = datetime.timezone(istTimeDelta, name="IST")
curr_time = datetime.datetime.now(tz=istTZObject).strftime('%d-%b-%Y %I:%M %p')

curr_prices = get_latest_crypto_prices()
curr_prices['usd'] = str(curr_prices['usd']) + \
    '<br>Ethereum: <br>INR: ₹' + str(eth_price_in_inr)

if float(curr_prices['inr']) < 3400000.0 or float(curr_prices['inr']) > 3450000:
    print(requests.post(IFTTT_URL + os.getenv('ifttt_api_key'),
                        data={'value1': curr_time, 'value2': curr_prices['inr'], 'value3': curr_prices['usd']}).content.decode('ascii'))
