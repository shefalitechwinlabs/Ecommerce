from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class Address(models.Model):
    address = models.TextField(null=True)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    created_by = models.ForeignKey(ExtendUser,on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.created_by.username

class Profile(models.Model):
    bio = models.TextField(null=True)
    image = models.ImageField(null=True)
    created_by = models.ForeignKey(ExtendUser,on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.created_by.username