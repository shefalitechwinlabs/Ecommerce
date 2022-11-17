from django.contrib import admin
from django.urls import path, include
from products.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('electronics/', electrnoics, name='electrnoics'),
    path('fashion/', fashion, name='fashion'),
    path('home_uses/', home_uses, name='home_uses'),
    path('gadgets/', gadgets, name='gadgets'),
    path('add_to_my_collections/<id>', electronics_collections, name='electronics_collections')
]
