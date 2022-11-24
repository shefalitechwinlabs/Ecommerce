from django.shortcuts import render, redirect
from django.http import JsonResponse
from accounts.models import ExtendUser, Profile
from .models import *
from django.shortcuts import get_object_or_404,render
from django.contrib import messages
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def home(request):
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        return render(request, 'main/home.html', {'profile':profile}) 
    else:
        return render(request, 'main/home.html')

@api_view('GET', 'POST')
def products_list(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({'products': serializer.data})

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.Http_201_CREATED)

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

# def collections(request):
#     if 'username' in request.session:
#         user = request.user
#         product = Collections.objects.filter(user=user)
#         context = {
#             'collections': product,
#         }
#         return render(request, 'accounts/profile/profile.html', context)
#     else:
#         return redirect('/accounts/login')



