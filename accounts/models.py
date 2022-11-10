from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage


class ExtendUser(AbstractUser):
    fs = FileSystemStorage(location='/media/')
    bio = models.TextField()
    image = models.ImageField(storage=fs, null=True, blank=True)


    def __str__(self):
        return self.username

class Profile(models.Model):
    name = models.OneToOneField(ExtendUser,on_delete=models.CASCADE, null=True)

    def __str__(self):
        fullname = self.name.first_name + self.name.last_name
        return fullname

class Address(models.Model):
    address = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Address"

    def __str__(self):
        return self.address.name.username