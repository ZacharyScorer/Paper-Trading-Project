from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from stock.viewsClasses import display_stock
from .models import PaperTradeTicker, PaperTrade
from .viewsClasses import get_current_portfolio


# Displays the user's paper trading portfolio and buys/sells shares if a POST call is made
@login_required
def home(request):
    user = request.user

    get_money = PaperTrade.objects.all()

    if request.method == 'POST':
        amount = request.POST.get('amount')
        price = request.POST.get('price')
        ticker = request.POST.get('ticker')
        buy_or_sell = request.POST.get('buy_or_sell')

        if buy_or_sell == 'buy':
            # If the user already owns shares of this stock
            if PaperTradeTicker.objects.filter(ticker=ticker).exists():
                ticker_info = display_stock(ticker)
                p = PaperTradeTicker.objects.filter(ticker=ticker)
                # Update price
                p.update(price=round(((p[0].price * p[0].amount) + (ticker_info.price * float(amount))) / (
                            p[0].amount + float(amount)), 2))
                PaperTradeTicker.objects.bulk_update(p, ['price'])
                # Update amount
                p.update(amount=p[0].amount + float(amount))
                PaperTradeTicker.objects.bulk_update(p, ['amount'])

            else:
                p = PaperTradeTicker(papertrade=user.papertrade, ticker=ticker, price=price, amount=amount)
                p.save()

            # Update money
            get_money.update(money=round(get_money[0].money - (float(price) * float(amount)), 2))
            PaperTrade.objects.bulk_update(get_money, ['money'])

        elif buy_or_sell == 'sell':
            # Only sell if the user owns shares of the stock
            if PaperTradeTicker.objects.filter(ticker=ticker).exists():
                p = PaperTradeTicker.objects.filter(ticker=ticker)

                if p[0].amount >= float(amount):
                    # Update amount
                    p.update(amount=p[0].amount - float(amount))
                    PaperTradeTicker.objects.bulk_update(p, ['amount'])

                    # Update money
                    get_money.update(money=round(get_money[0].money + (float(price) * float(amount)), 2))
                    PaperTrade.objects.bulk_update(get_money, ['money'])

    context = {'data': get_current_portfolio(request), 'money': get_money[0].money}

    return render(request, 'paper_trade/paper_trade_home.html', context)


def search(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('ticker').upper()

        context['data'] = display_stock(name)

    return render(request, 'paper_trade/paper_trade_search.html', context)
