from django.contrib import admin
from django.urls import path, include
from products.views import *

urlpatterns = [
    path('', home, name='home'),
    #path('products/', products, name='products'),
    path('electronics/', electronics, name='electronics'),
    path('fashion/', fashion, name='fashion'),
    path('home_uses/', home_uses, name='home_uses'),
    path('gadgets/', gadgets, name='gadgets'),
    path('add_collections/', add_collections, name='add_collections'),
    path('remove_collections/<id>', remove_collections, name='remove_collections'),
    path('clear_collections/', clear_collections, name='clear_collections')
]
