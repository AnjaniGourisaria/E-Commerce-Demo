from django.contrib import admin
from .models import (Product , Contacts , Customer , Cart , OrderPlaced , Wish, Coupon)
# Register your models here.
from django.utils.html import format_html
# admin.site.register(ProdDetails)

#Customer Registraiton
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','name','phone','station','locality','city','zipcode','state','date','is_deleted')
    list_display_links= ('id','user','name','phone','station','locality','city','zipcode','state','date')
    list_filter = ('is_deleted','date')
    save_on_top = True
    list_per_page = 20
    search_fields = ('id','user','name','phone','station','locality','city','zipcode','state','date','is_deleted')
        
admin.site.register(Customer,CustomerModelAdmin)

#Product Registraiton
class ProductModelAdmin(admin.ModelAdmin):
    readonly_fields = ('photo',)
    list_display= ('id','product_name','category','sub_category','brand','price','dprice','publish_date','photo','stock','is_deleted')
    list_display_links=  ('id','product_name','category','sub_category','brand','price','dprice','publish_date','photo','stock','is_deleted')
    list_filter = ('is_deleted','publish_date')
    save_on_top = True
    list_per_page = 20
    search_fields = ('id','product_name','category','sub_category','brand','price','dprice','publish_date','photo','stock','is_deleted')
    
    def photo(self,obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:100px;width:100px">')
    
admin.site.register(Product,ProductModelAdmin)

#Contacts Registraiton

class ContactsModelAdmin(admin.ModelAdmin):
    list_display= ('id','username','email','phone','publish_date','is_deleted')
    list_display_links= ('id','username','email','phone','publish_date','is_deleted')
    list_filter = ('is_deleted','publish_date')
    save_on_top = True
    list_per_page = 20
    search_fields = ('id','username','email','phone','publish_date','is_deleted')
    
admin.site.register(Contacts ,ContactsModelAdmin)


#Cart Registraiton
class CartModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','product','quantity','is_deleted')
    list_display_links = ('id','user','product','quantity','is_deleted')
    list_filter = ('is_deleted',)
    save_on_top = True
    list_per_page = 20
    search_fields =('id','user','product','quantity','is_deleted')
    
admin.site.register(Cart,CartModelAdmin)


#OrderPlaced Registraiton
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','customer','product','quantity','ordered_date','status','is_deleted')
    list_display_links = ('id','user','customer','product','quantity','ordered_date','status','is_deleted')
    list_filter = ('is_deleted','ordered_date')
    save_on_top = True
    list_per_page = 20
    search_fields =('id','user','customer','product','quantity','ordered_date','status','is_deleted')
admin.site.register(OrderPlaced , OrderPlacedModelAdmin)



class WishModelAdmin(admin.ModelAdmin):
    list_display= ('id','user','product','is_deleted')
    list_display_links = ('id','user','product','is_deleted')
    list_filter = ('is_deleted','created_date')
    save_on_top = True
    list_per_page = 20
    search_fields = ('id','user','product','is_deleted')
admin.site.register(Wish, WishModelAdmin)

class CouponModelAdmin(admin.ModelAdmin):
    list_display= ('id','discount','product','is_deleted')
    list_display_links =  ('id','discount','product','is_deleted')
    list_filter = ('is_deleted','created_date')
    save_on_top = True
    list_per_page = 20
    search_fields = ('id','discount','product','is_deleted')

admin.site.register(Coupon,CouponModelAdmin )