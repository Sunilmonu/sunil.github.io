from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
class products(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='default.jpg',upload_to='uploads')
    sale=models.BooleanField(default=False)
    trending=models.BooleanField(default=False)


class cartmodel(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    image=models.ImageField(default='default.jpg',upload_to='uploads')
    sale=models.BooleanField(default=False)
    trending=models.BooleanField(default=False)
    # quantity=models.IntegerField(default=1)
    # totalprice=models.IntegerField(default=0)
    # host=models.ForeignKey(User,on_delete=models.CASCADE)