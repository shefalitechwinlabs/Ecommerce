from django.db import models
from accounts.models import ExtendUser


category = [
        ('Fashion', 'fashion'),
        ('Gadgets', 'gadgets'),
        ('Home', 'home'),
        ('Electronics', 'electronics'),
    ]

class Products(models.Model):
    title = models.CharField(max_length=50, default='title of product')
    description = models.CharField(max_length=500, default='description of product')
    price = models.CharField(max_length=10, default=100)
    image = models.ImageField(upload_to='home_images', null=True)
    product_category = models.CharField(max_length=20,choices=category, default='random')

    class Meta():
        verbose_name = "Product" 

    def __str__(self):
        return self.product_category

class Electronics(models.Model):
    electronics_item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "Electronic" 

    def __str__(self):
        return self.title


class Home(models.Model):
    home_item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "home" 

class Gadgets(models.Model):
    gadgets_item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "Gadget" 

class Fashion(models.Model):
    fashion_item = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = "fashion" 

class Collections(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, null=True)
    added_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta():
        verbose_name = "Collection" 

    def __str__(self):
        return self.added_by.username