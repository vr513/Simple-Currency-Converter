import requests
import sys

url = 'https://api.exchangerate-api.com/v4/latest/USD'


def convert(from_currency, to_currency, amount):
    data = requests.get(url).json()
    rates = data["rates"]
    initial_amount = amount
    amount = amount / rates[from_currency]
    amount = round(amount * rates[to_currency], 2)
    print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
    return amount


from_country = sys.argv[1]
to_country = sys.argv[2]
amount = int(sys.argv[3])

new_amount = convert(from_country, to_country, amount)
