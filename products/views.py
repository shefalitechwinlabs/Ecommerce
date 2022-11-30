from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import requests
from accounts.models import ExtendUser, Profile
from .models import *
from django.shortcuts import get_object_or_404,render
from django.contrib import messages
from .serializers import ProductSerializer
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# third party api code
url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

querystring = {"query":"<REQUIRED>"}

headers = {
    "X-RapidAPI-Key": "8eed531a55msh7f803c88a14e1a0p13c019jsnc3cf0ec8acb9",
    "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

def home(request):
    # to show profile in navbar or else sign in
    print(response.text)
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        return render(request, 'main/home.html', {'profile':profile}) 
    else:
        return render(request, 'main/home.html')

def electronics(request):
    electronics_obj = Products.objects.filter(product_category='Electronics')
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        context = {
            'products': electronics_obj,
            'profile': profile
        }
        return render(request, 'main/products/electronics.html', context) 
    else:
        context = {
            'products': electronics_obj,
        }
        return render(request, 'main/products/electronics.html', context)

def gadgets(request):
    gadgets_obj = Products.objects.filter(product_category='Gadgets')
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        context = {
            'products': gadgets_obj,
            'profile': profile
        }
        return render(request, 'main/products/gadgets.html', context) 
    else:
        context = {
            'products': gadgets_obj,
        }
        return render(request, 'main/products/gadgets.html', context)

def home_uses(request):
    home_obj = Products.objects.filter(product_category='Home')
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        context = {
            'products': home_obj,
            'profile': profile
        }
        return render(request, 'main/products/home_uses.html', context) 
    else:
        context = {
            'products': home_obj,
        }
        return render(request, 'main/products/home_uses.html', context)

def fashion(request):
    fashion_obj = Products.objects.filter(product_category='Fashion')
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        context = {
            'products': fashion_obj,
            'profile': profile
        }
        return render(request, 'main/products/fashion.html', context) 
    else:
        context = {
            'products': fashion_obj,
        }
        return render(request, 'main/products/fashion.html', context)

def add_collections(request):
    if 'username' in request.session:
        id = request.GET.get('id')
        page = request.GET.get('page')
        print(id, page)
        try:
            Collections.objects.get(product_id=id)
            messages.warning(request, 'product exists')
            return redirect(page)
        except:
            #obj = get_object_or_404(Collections, id = id)
            user = request.user
            product = Products.objects.get(id=id)
            collection = Collections(product=product, added_by=user)
            collection.save()
            messages.success(request, 'products added successfully')
            return redirect(page)
    else:
        return redirect('/accounts/login')

def remove_collections(request, id):
    if 'username' in request.session:
        obj = get_object_or_404(Collections, id = id)
        if obj:
            # delete collections
            obj.delete()
            messages.success(request, 'product removed sucessfully')
            return redirect('/profile')
        else:
            messages.error(request, 'product not removed successfully')
            return redirect('/profile')
    else:
        return redirect('/accounts/login')

def clear_collections(request):
    if 'username' in request.session:
        Collections.objects.all().delete()
        messages.success(request, 'collections cleared')
        return redirect('/profile')
    else:
        return redirect('/accounts/login')

def calculator(request):
    return render(request, 'main/calculator.html')

# api view functions
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        data = serializers.serialize("json", Products.objects.all())
        return JsonResponse(json.loads(data), safe=False)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def products_category(request, category):
    products = Products.objects.filter(product_category=category)
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data})
