import locale
import datetime
import os
import requests

from dotenv import load_dotenv
load_dotenv()

locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

BITCOIN_API_URL = 'https://api.wazirx.com/api/v2/tickers'
IFTTT_URL = 'https://maker.ifttt.com/trigger/crypto_alert/with/key/'


def get_latest_crypto_prices():
    global eth_price_in_inr
    response = requests.get(BITCOIN_API_URL).json()
    btc_price_in_inr = locale.currency(
        float(response['btcinr']['last']), grouping=True)
    eth_price_in_inr = locale.currency(
        float(response['ethinr']['last']), grouping=True)
    doge_price_in_inr = locale.currency(
        float(response['dogeinr']['last']), grouping=True)
    return {'bitcoin': btc_price_in_inr, 'ethereum': eth_price_in_inr, 'doge': doge_price_in_inr}


istTimeDelta = datetime.timedelta(hours=5, minutes=30)
istTZObject = datetime.timezone(istTimeDelta, name="IST")
curr_time = datetime.datetime.now(tz=istTZObject).strftime('%d-%b-%Y %I:%M %p')

curr_prices = get_latest_crypto_prices()
message_to_be_posted = "<b>Crypto Price Alert " + str(curr_time)
message_to_be_posted += "</b><br><b>Bitcoin: </b><code><b>" + \
    str(curr_prices['bitcoin'])
message_to_be_posted += "</b></code><br><b>Ethereum: </b><code><b>" + \
    str(curr_prices['ethereum'])
message_to_be_posted += "</b></code><br><b>DogeCoin: </b><code><b>" + \
    str(curr_prices['doge']) + "</b></code>"


print(
    requests.post(
        IFTTT_URL + os.getenv('ifttt_api_key'),
        data={'value1': message_to_be_posted}).content.decode('ascii'))
