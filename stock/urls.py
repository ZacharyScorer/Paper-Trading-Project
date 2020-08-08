from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="stock-home"),
    path('search', views.search, name="stock-search"),
]