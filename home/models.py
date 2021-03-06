from django.db import models
from datetime import datetime   
from django.contrib.auth.models import User 
from django.core.validators import MaxLengthValidator,MinValueValidator
from django.utils.html import format_html
# from ckeditor.fields import RichTextField
# # msg = RichTextField(max_length=900,default="")
#   
# Create your models here.

class Contacts(models.Model):
    username = models.CharField(max_length=15,default="")
    email = models.EmailField(max_length=30,default="")
    phone = models.IntegerField(default="")
    msg = models.CharField(max_length=900,default="")
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
 
        
STATION = (
    ('Home','Home'),
    ('Work','Work'),
    ('Others','Others'),
)


class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    station = models.CharField(choices=STATION,max_length=20)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField()
    state = models.CharField(max_length=30)
    date = models.DateTimeField(default=datetime.now,blank=True)
    is_deleted = models.BooleanField(default=False)
    # created_date = models.DateField(auto_created=True,blank=True,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_id(self):
        return str(self.id)
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=40,default="")
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=40,default="")
    brand = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    dprice = models.FloatField()
    description = models.CharField(max_length=400,default="")
    publish_date= models.DateTimeField(default=datetime.now,blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='img/',default="",blank=True)
    image2 = models.ImageField(upload_to='img/',default="",blank=True)
    image3 = models.ImageField(upload_to='img/',default="",blank=True)
    image4 = models.ImageField(upload_to='img/',default="",blank=True)
    is_deleted = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.id)

    


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateField(auto_created=True,blank=True,null=True)
    
    def __str__(self):
         return str(self.id)

    @property 
    def get_q_and_dprice(self):
        tempamont = self.quantity * self.product.dprice
        return tempamont


class OrderPlaced(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='Pending')
    is_deleted = models.BooleanField(default=False)
    
    @property
    def customerid(self):
        return self.customer.name
    
    @property
    def productid(self):
        return self.product.product_name
    
    @property
    def photoid(self):
        return self.product.image.url
    
    
    
class Wish(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateField(auto_created=True,blank=True,null=True)
    def __str__(self):
        return str(self.id)
    
class Coupon(models.Model):
    discount = models.CharField(max_length=7,default=""), 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateField(auto_created=True,blank=True,null=True)