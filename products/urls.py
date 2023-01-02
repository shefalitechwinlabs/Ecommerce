from django.contrib import admin
from django.urls import path, include
from products.views import *

urlpatterns = [
    path('', home, name='home'),
    path('electronics/', electronics, name='electronics'),
    path('fashion/', fashion, name='fashion'),
    path('home_uses/', home_uses, name='home_uses'),
    path('gadgets/', gadgets, name='gadgets'),
    path('add_collections/', add_collections, name='add_collections'),
    path('remove_collections/<id>', remove_collections, name='remove_collections'),
    path('clear_collections/', clear_collections, name='clear_collections'),
    path('products/', products, name='products'),
    path('products/<category>', products_category, name='products_category'),
    # path('chatbot/', chatbot_view, name='chatbot_view'),
    # path('chatbot/response', chatbot_msg, name='chatbot_msg'),
    #path('products_create', products_creation, name='products_creation'),
]
