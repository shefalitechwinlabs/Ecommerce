from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
import bson
import re
import pandas as pd
import requests
import subprocess
import os
import pymongo
from accounts.models import ExtendUser, Profile
from .models import *
from django.shortcuts import get_object_or_404,render
from django.contrib import messages
from .serializers import ProductSerializer
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic import View
# from chatterbot import ChatBot
# from chatterbot.ext.django_chatterbot import settings
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import imdb


# third party api code
url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"

querystring = {"query":"<REQUIRED>"}

headers = {
    "X-RapidAPI-Key": "8eed531a55msh7f803c88a14e1a0p13c019jsnc3cf0ec8acb9",
    "X-RapidAPI-Host": "bloomberg-market-and-financial-news.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

from pymongo import MongoClient
import subprocess

def home(request):
    # to show profile in navbar or else sign in
    print(response.text)
    if 'username' in request.session:
        user = request.user
        profile = Profile.objects.get(created_by=user)
        return render(request, 'main/home.html', {'profile':profile}) 
    else:
        return render(request, 'main/home.html')

def create_backup_with_subprocess(request):
    client = MongoClient('localhost', 27017)
    databases = client.list_databases()
    for db in databases:
        db_name = db['name']
        subprocess.run(['mongodump',  '--out=/Users/admin/Downloads/Ecommerce_backup/' + db_name, '-d=' + db_name])
    return HttpResponse('backup_created')

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

# from chatterbot.trainers import ChatterBotCorpusTrainer
# chatbot=ChatBot('mania',trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# chatbot = ChatBot('Mania')

# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train based on the english corpus
# trainer.train("chatterbot.corpus.english")

# @csrf_exempt
# def chatbot_msg(request):
# 	response = {'status': None}

# 	if request.method == 'POST':
# 		data = json.loads(request.body)
# 		message = data['message']

# 		chat_response = chatbot.get_response(message).text
# 		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
# 		response['status'] = 'ok'

# 	else:
# 		response['error'] = 'no post data found'

# 	return HttpResponse(
# 		json.dumps(response),
# 			content_type="application/json"
# 		)


# def chatbot_view(request):
# 	context = {'title': 'Mania Chatbot Version 1.0'}
# 	return render(request, 'main/chatbot/chatbot.html', context)

@csrf_exempt
def add_collections(request):
    if 'username' in request.session:
        id = request.GET.get('id')
        print(id)
        try: # if product already exist
            Collections.objects.get(product_id=id)
            return JsonResponse({"type":"Warning","message":"product exists"})
        except: # if product not exist
            user = request.user
            product = Products.objects.get(id=id)
            collection = Collections(product=product, added_by=user)
            collection.save()
            return JsonResponse({"type":"Success",'message':'product added to my collections'})
    else:
        return JsonResponse({'type':'Warning','message':'You need to login first'})

def remove_collections(request, id):
    if 'username' in request.session:
        obj = get_object_or_404(Collections, id = id)
        if obj:
            # delete collections
            obj.delete()
            return JsonResponse({'type':'Success','message':'Product removed!'})
        else:
            return JsonResponse({'type':'Warning','message':'Product not removed!'})
    else:
        return redirect('/accounts/login')

def clear_collections(request):
    if 'username' in request.session:
        obj = Collections.objects.all()
        if obj:
            Collections.objects.all().delete()
            return JsonResponse({'type':'Success','message':'Collections cleared!'})
        else:
            return JsonResponse({'type':'Warning','message':'No collections to clear!'})
    else:
        return redirect('/accounts/login')

def calculator(request):
    return render(request, 'main/calculator.html')

@csrf_exempt
def table(request):
    search = imdb.IMDb()
    # Using the Search movie method
    movies = search.search_movie('koyla')
    print(type(movies))
    for movie in movies:
        print(type(movie))
    return render(request, 'random/table.html')

@csrf_exempt
def random(request):
    products_obj = Products.objects.all()
    category = []
    for i in range(len(products_obj)):
        category.append(products_obj[i].product_category)
    categories = set(category)
    if request.method == 'POST':
        product_catrgories = request.POST.getlist('categories[]')
        product_titles = request.POST.getlist('products[]')
        if 'categories[]' in request.POST:
            print('categories contain')
            product_titles = []
            if not product_catrgories :
                product_titles = 0
            elif 'selectall' in product_catrgories:
                for i in products_obj:
                    product_titles.append(i.title)
            else:
                for product_category in product_catrgories:
                    products = Products.objects.filter(product_category=product_category)
                    for product_title in products:
                        product_titles.append(product_title.title)
            return JsonResponse(product_titles, safe=False)
        if 'products[]' in request.POST or not product_titles:
            print('products contain')
            product_details = []
            if not product_titles :
                product_details = 0
            else:
                for product_title in product_titles:
                    products = Products.objects.filter(title=product_title)
                    for product_description in products:
                        product_details.append(product_description.description)
            return JsonResponse(product_details, safe=False)
        if not product_titles and not product_catrgories:
            product_details = 0
            product_titles = 0
            return JsonResponse(product_titles,product_details, safe=False)
    else:
        context = {
            'categories': categories
        }
        return render(request, 'random/random.html', context)

def datatables(request):
    return render(request, 'random/datatables.html')

def loading_bar(request):
    return render(request, 'Loadingbar/index.html')

def google_file_upload(request):
    if request.method=='POST':
        file = request.file
        print(file)
        return HttpResponse('uploaded')
    return render(request, 'random/google_file_upload.html')


# api view functions
# @api_view(['GET', 'POST'])
@csrf_exempt
def products(request):
    if request.method == 'GET':
        draw = request.GET['draw']
        row_per_page = request.GET['length']
        start = request.GET['start'] # records needed for per page
        column_index = request.GET.get('order[0][column]')

        products_obj = Products.objects.all()
        products_obj_values = products_obj.values()
        
        list_of_products_data = []

        for product_dict in products_obj_values:
            DT_row = {
                "DT_RowId": "row_"+str(product_dict['id']),
                "DT_RowData": {
                    "pkey": product_dict['id']
                }, 
            }
            product_dict.pop('id')
            DT_row.update(product_dict)
            list_of_products_data.append(DT_row)
        df_list_of_products_data = pd.DataFrame(list_of_products_data)

        # sorting by columns
        column_name = request.GET.get(f'columns[{column_index}][data]') # column's name based on column index
        column_sort_order = request.GET.get('order[0][dir]')
        if column_sort_order == 'desc':
            sort_order = False
        else:
            sort_order = True
        df_list_of_products_data = df_list_of_products_data.sort_values(by=[column_name], ascending=sort_order)
        list_of_products_data = df_list_of_products_data.to_dict(orient='records')

        # searching by regex
        search = request.GET.getlist('search[value]')
        if search[0]:
            columns_list = df_list_of_products_data.columns.to_list()
            search_filter = df_list_of_products_data[columns_list].apply(
                            lambda x: x.str.contains(
                                f'{search[0]}',
                                regex=True,
                            )
                        ).any(axis=1)
            search_filtered = df_list_of_products_data[search_filter].to_dict(orient='records')
            list_of_products_data = search_filtered

        total = products_obj.count()
        total_filter = len(list_of_products_data)
        list_of_products_data = list_of_products_data[ int(start): int(start) + int(row_per_page) ]
        list_of_products = list_of_products_data
        
        products_data = {
            "draw": int(draw),
            "recordsTotal": total,
            "recordsFiltered": total_filter,
            "data": list_of_products
        }
        return JsonResponse(products_data, safe=False)

    # if request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def products_category(request, category):
    products = Products.objects.filter(product_category=category)
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data})

# CREATE BACKUP
def create_backup(request):

    # function to dump data for particular database
    def dump(collections, client, db_name, path):
        db = client[db_name]
        for collection in collections:
            with open(f"{path}/{db_name}/{collection}.bson","wb+") as f:
                for data in db[collection].find():
                    f.write(bson.BSON.encode(data))

    # configure credentials / db name
    client = pymongo.MongoClient('localhost', 27017)
    databases = client.list_databases()

    # loop for iterate all database as db
    for db in databases:
        db_name = db['name']
        db = client[db_name]
        path = os.path.dirname(f'backup/')
        os.makedirs(f'{path}/{db_name}', exist_ok=True)

        collections = db.list_collection_names()
        # call dump function by passing params of collections, configured db, db name and backup folder path 
        dump(collections, client, db_name, path)

    return HttpResponse('backup_created')

def restore_backup(request):

    # func to restore db 
    def restore(path, client, db_name):
        db = client[db_name]
        for coll in os.listdir(path):
            if coll.endswith('.bson'):
                try: # restoring empty collections throw an error 
                    with open(os.path.join(path, coll), 'rb+') as f:
                        db[coll.split('.')[0]].insert_many(bson.decode_all(f.read()))
                except:
                    pass

    client = pymongo.MongoClient('localhost', 27017)
    databases = client.list_databases()

    # "backup/" folder needs to be created manually
    path = os.path.dirname(f'backup/')
    for db in databases:
        db_name = db['name']
        db = client[db_name]
        path = f'backup/{db_name}'
        restore(path, client, db_name)

    return HttpResponse('backup_restored')


# def products(request, category):
#     products = Products.objects.filter(product_category=category)
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse({'products': serializer.data})

# cronjob
python_path = subprocess.run(["which", "python"], stdout=subprocess.PIPE).stdout.strip().decode("utf-8")
command = "/usr/bin/python /Downloads/Ecommerce/products/management/commands/command.py cron"
def cron_script(request):
    # subprocess.run(['', 'crontab -e'])
    return render(request, "random/cronjob.html")

def run_command(command):
    result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode("utf-8").strip()

def run_cron_script(request):
    subprocess.run([python_path, "/Downloads/Ecommerce/products/management/commands/command.py cron"])
    cron_job = f"* * * * * {command}\n"
    cron_file = "/etc/crontab" if os.name == "posix" else "/usr/lib/cron/tabs/techwin"
    with open(cron_file, "a") as f:
        f.write(cron_job)
    return render(request, "random/cronstart.html", {})

def stop_cron_script(request):
    subprocess.run([python_path, "products/cron_job.py", "stop"])
    cron_jobs = run_command("crontab -l").split("\n")
    cron_file = "sudo nano /etc/crontab" if os.name == "posix" else "/usr/lib/cron/tabs/techwin"
    with open(cron_file, "w") as f:
        for job in cron_jobs:
            if command not in job:
                f.write(job + "\n")
    return render(request, "random/cronstop.html", {})
