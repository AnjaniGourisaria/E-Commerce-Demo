from django.contrib import admin
from .models import (Product , Contacts , Customer , Cart , OrderPlaced , Wish)
# Register your models here.
# admin.site.register(ProdDetails)

#Customer Registraiton
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    model = Customer
    list_dislay= ['id','user','name','phone','station','locality','city','zipcode','state','date']

#Product Registraiton
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_dislay= ['id','product_name','category','sub_category','brand','price','dprice','publish_date','stock','date']
    
#Contacts Registraiton

class ContactsModelAdmin(admin.ModelAdmin):
    list_dislay= ['id','username','email','phone','publish_date']
    
admin.site.register(Contacts ,ContactsModelAdmin)


#Cart Registraiton
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_dislay= ['id','user','product','quantity']
    

#OrderPlaced Registraiton
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_dislay= ['id','user','customer','product','quantity','ordered_date','status']

admin.site.register(Wish)
