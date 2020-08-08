from django.db import models
from django.contrib.auth.models import User


# Each user has one PaperTrade model that contains all of their PaperTradeTickers
class PaperTrade(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.FloatField(User, default=5000.0)

    def __str__(self):
        return f"{self.user.username}'s Paper Trader"


class PaperTradeTicker(models.Model):
    papertrade = models.ForeignKey(PaperTrade, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=5)
    price = models.FloatField()
    amount = models.FloatField()

    def get_ticker(self):
        return self.ticker

    def get_price_bought(self):
        return self.price

    def get_amount_bought(self):
        return self.amount
