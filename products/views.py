from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.models import ExtendUser, Profile
from .models import *


def home(request):
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        return render(request, 'main/index.html', {'profile':profile}) 
    else:
        return render(request, 'main/index.html')

def products(request):
    electronics = Electronics.objects.all()
    gadgets = Gadgets.objects.all()
    home = Home.objects.all()
    fashion = Fashion.objects.all()
    return render(request, 'main/products/products.html')

def electrnoics(request):
    electronics_obj = Electronics.objects.all()
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
    gadgets_obj = Gadgets.objects.all()
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
    home_obj = Home.objects.all()
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
    fashion_obj = Fashion.objects.all()
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

def electronics_collections(request, id):

    
    return redirect('/profile')


