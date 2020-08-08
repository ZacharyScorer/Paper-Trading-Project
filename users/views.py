from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm
from .models import WatchlistTicker
from .viewsClasses import get_current_watchlist


# Creates a user account
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Verifies the user is logged in and then pulls their watchlist data
@login_required
def watchlist(request):
    user = request.user

    if request.method == 'POST':
        add_or_remove = request.POST.get('add_or_remove')
        ticker_received = request.POST.get('ticker')
        if add_or_remove == 'add':
            p = WatchlistTicker(watchlist=user.watchlist, ticker=ticker_received)
            p.save()

        elif add_or_remove == 'remove':
            p = WatchlistTicker.objects.filter(ticker=ticker_received)
            p.delete()

    context = {'data': get_current_watchlist(request)}

    return render(request, 'users/watchlist.html', context)
