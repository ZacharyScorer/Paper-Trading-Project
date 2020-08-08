from django.urls import path
from . import views

urlpatterns = [
    path('paper_trading/', views.home, name="paper_trade-home"),
    path('paper_trading/search', views.search, name="paper_trade-search"),
]
