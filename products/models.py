from django.db import models
from accounts.models import ExtendUser

class Fashion(models.Model):
    title = models.CharField(max_length=50, default='title of product')
    description = models.CharField(max_length=500, default='description of product')
    price = models.CharField(max_length=10, default=100)
    image = models.ImageField(upload_to='fashion_images', null=True)

    class Meta():
        verbose_name = "Fashion" 

    def __str__(self):
        return self.title

class Electronics(models.Model):
    title = models.CharField(max_length=50, default='title of product')
    description = models.CharField(max_length=500, default='description of product')
    price = models.CharField(max_length=10, default=100)
    image = models.ImageField(upload_to='electronic_images', null=True)

    class Meta():
        verbose_name = "Electronic" 

    def __str__(self):
        return self.title

class Gadgets(models.Model):
    title = models.CharField(max_length=50, default='title of product')
    description = models.CharField(max_length=500, default='description of product')
    price = models.CharField(max_length=10, default=100)
    image = models.ImageField(upload_to='gadgets_images', null=True)

    class Meta():
        verbose_name = "Gadget" 

    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField(max_length=50, default='title of product')
    description = models.CharField(max_length=500, default='description of product')
    price = models.CharField(max_length=10, default=100)
    image = models.ImageField(upload_to='home_images', null=True)

    class Meta():
        verbose_name = "Home" 

    def __str__(self):
        return self.title

class Collections(models.Model):
    electronics = models.ForeignKey(Electronics, on_delete=models.CASCADE, null=True)
    home = models.ForeignKey(Home, on_delete=models.CASCADE, null=True)
    gadgets = models.ForeignKey(Gadgets, on_delete=models.CASCADE, null=True)
    fashion = models.ForeignKey(Fashion, on_delete=models.CASCADE, null=True)
    user_collection = models.OneToOneField(ExtendUser, on_delete=models.CASCADE, null=True )

    class Meta():
        verbose_name = "Collection"

    def __str__(self):
        return self.user_collection.username

