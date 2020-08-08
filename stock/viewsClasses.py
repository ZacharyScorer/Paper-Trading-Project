import os
import requests


# Stores the data for the desired stock in a Ticker object
class Ticker:
    def __init__(self, quote, company_profile, gain):
        self.ticker = company_profile['ticker']
        self.price = quote['c']
        self.gain = gain
        self.prev_close_price = quote['pc']
        self.change = round(self.price - self.prev_close_price, 2)
        self.change_percentage = round(self.change / self.price * 100, 2)
        self.company_name = company_profile['name']


# Gets the data for the searched stock using a Ticker object to store and access it
def display_stock(name):
    api_key = os.getenv("FINNHUB_API_KEY")
    response = requests.get(f'https://finnhub.io/api/v1/quote?symbol={name}&token={api_key}')
    quote = response.json()
    price = quote['c']
    prev_close_price = quote['pc']
    response = requests.get(f'https://finnhub.io/api/v1/stock/profile2?symbol={name}&token={api_key}')
    company_profile = response.json()

    if price > prev_close_price:
        gain = 'positive'
        ticker = Ticker(quote, company_profile, gain)
    elif price == prev_close_price:
        gain = 'neutral'
        ticker = Ticker(quote, company_profile, gain)
    else:
        gain = 'negative'
        ticker = Ticker(quote, company_profile, gain)

    return ticker


# Created for each of the gainer/losers on the home page
class GainerLoser:
    def __init__(self, data, index, gain):
        self.ticker = data[index]['ticker']
        self.change = data[index]['changes']
        self.price = data[index]['price']
        self.change_percentage = data[index]['changesPercentage']
        self.name = data[index]['companyName']
        self.gain = gain
