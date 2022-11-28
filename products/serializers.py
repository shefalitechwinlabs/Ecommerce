from rest_framework import serializers
from .models import Products
from accounts.models import ExtendUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Products
        fields = ['title','description', 'price', 'image', 'product_category']

class ExtendUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = ExtendUser
        fields = "__all__"
