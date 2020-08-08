from django.shortcuts import render
from .viewsClasses import display_stock, GainerLoser
from users.viewsClasses import get_current_watchlist
from users.models import Watchlist, WatchlistTicker
import requests
import os


# These use Financial Modeling Prep api
# Gainers/losers on the home page
def home(request):
    # api_key = os.getenv('FMP_API_KEY')
    # # Gainer
    # response = requests.get("https://financialmodelingprep.com/api/v3/gainers?apikey={}".format(api_key))
    # data = response.json()
    # gain = []
    # for index in range(0, 5):
    #     gain.append(GainerLoser(data, index, True))
    #
    # # Loser
    # response = requests.get("https://financialmodelingprep.com/api/v3/losers?apikey={}".format(api_key))
    # data = response.json()
    # lose = []
    # for index in range(0, 5):
    #     lose.append(GainerLoser(data, index, False))
    #
    # context = {'gain': gain, 'lose': lose}
    # return render(request, 'stock/home.html', context)
    return render(request, 'stock/home.html')


# These use Finnhub.io
# Get data for the requested stock
def search(request):
    context = {}
    name = None
    in_watchlist = False

    if request.method == 'POST':
        name = request.POST.get('ticker').upper()
        watchlist_tickers = get_current_watchlist(request)

        for item in watchlist_tickers:
            if item.ticker == name:
                in_watchlist = True

        context['data'] = display_stock(name)
        context['watchlist'] = in_watchlist

    return render(request, 'stock/search.html', context)
