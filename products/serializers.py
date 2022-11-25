from rest_framework import serializers
from .models import Products
from accounts.models import ExtendUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Products
        fields = "__all__"

class ExtendUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = ExtendUser
        fields = ['username', 'email', 'password', 'confirm_password']
