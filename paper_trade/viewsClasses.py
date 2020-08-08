import os
import requests

from .models import PaperTrade


class Ticker:
    def __init__(self, ticker, amount, price, current_price):
        self.ticker = ticker
        self.amount = amount
        self.price = price
        self.current_price = current_price
        self.price_difference = round((current_price - price) * amount, 2)


# gets the data for each ticker already in the user's portfolio
def get_current_portfolio(request):
    user = request.user
    results = PaperTrade.objects.filter(user=user)

    portfolio_tickers = list(results[0].papertradeticker_set.values('ticker'))
    portfolio_amount = list(results[0].papertradeticker_set.values('amount'))
    portfolio_price = list(results[0].papertradeticker_set.values('price'))

    ticker_list = []
    index = 0

    while index < len(portfolio_tickers):
        api_key = os.getenv("FINNHUB_API_KEY")
        response = requests.get(f'https://finnhub.io/api/v1/quote?symbol={portfolio_tickers[index]["ticker"]}&token={api_key}')
        quote = response.json()
        current_price = quote['c']
        ticker_list.append(Ticker(portfolio_tickers[index]['ticker'],
                                  portfolio_amount[index]['amount'],
                                  portfolio_price[index]['price'],
                                  current_price))
        index += 1

    return ticker_list
