from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField 
from datetime import datetime    

# Create your models here.
class Details(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=40,default="")
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=40,default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=400,default="")
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/',default="")
    
    def __str__(self):
        return self.product_name

# class SignUp(models.Model):
#     username = models.CharField(max_length=15,default="")
#     email = models.EmailField(max_length=30)
#     password = models.CharField(max_length=30)
#     reppassword = models.CharField(max_length=30)
#     phone = models.IntegerField(max_length=11)
    
#     def __str__(self):
#         return self.username

class Contacts(models.Model):
    username = models.CharField(max_length=15,default="")
    email = models.EmailField(max_length=30,default="")
    phone = models.IntegerField(default="")
    msg = models.CharField(max_length=900,default="")
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.username