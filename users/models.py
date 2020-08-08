from django.db import models
from django.contrib.auth.models import User


# Each user has one Watchlist that contains multiple WatchlistTickers
class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"


class WatchlistTicker(models.Model):
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)

    def get_tickers(self):
        return self.ticker
