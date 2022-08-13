import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
response = requests.get(URL).json()
coin = response.get('data')

print(coin.get('closing_price'))
