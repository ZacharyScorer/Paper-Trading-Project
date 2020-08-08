from stock.viewsClasses import display_stock
from .models import Watchlist


# Gets all of the stocks and their respective data in the user's watchlist
def get_current_watchlist(request):
    user = request.user
    results = Watchlist.objects.filter(user=user)
    watchlist_tickers = list(results[0].watchlistticker_set.values('ticker'))

    ticker_list = []
    index = 0

    while index < len(watchlist_tickers):
        ticker_list.append(display_stock(watchlist_tickers[index]['ticker']))
        index += 1

    return ticker_list
