from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):

    def __str__(self):
        return self.username

address_choices = [
        ('Home', 'home'),
        ('Office', 'office'),
        ('Other', 'other'),
    ]

class Address(models.Model):
    address_type = models.CharField(max_length=20,choices=address_choices, default='Home')
    building = models.TextField(null=True)
    locality = models.CharField(max_length=50, null=True)
    sector = models.CharField(max_length=50, null=True)
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
    name = models.CharField(max_length=150, default='name yet to be updated')
    bio = models.TextField(default='bio yet to be updated')
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/no_image.png')
    created_by = models.OneToOneField(ExtendUser,on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.created_by.username
        