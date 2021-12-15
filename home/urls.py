"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
# from home import views as view_as
from home import views
from home.views import CustumerRegestrationView

urlpatterns = [
    # path("electronic",views.electronic,name='electronic'),
    # path('',views.ProductView.as_view(),name='home'),
    # path("fashion",views.fashion,name='fashion'),
    # path("sign_up",views.sign_up,name='sign_up'),
    # path("jewellery",views.jewellery,name='jewellery'),
    #path("minus_cart",views.minus_cart,name="minus_cart"),
    #path("plus_cart",views.plus_cart),
    # path("update_cart",views.update_cart),
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("home",views.index,name='home'),
    path("help",views.help,name='help'),
    path("search",views.search,name='search'),
    path("addcart",views.addcart,name='addcart'),
    path('cart/',views.sync_cart,name='sync_cart'),
    path('remove_cart',views.remove_cart,name='remove_cart'),
    path('sign_up',views.CustumerRegestrationView.as_view(),name='sign_up'),
    path("shop",views.shop,name='shop'),
    path("checkout",views.checkout,name='checkout'),
    path("login",views.login,name='login'),
    path("sign_in",views.sign_in,name='sign_in'),
    path("log_out",views.log_out,name='log_out'),
    path("contactus",views.contactus,name='contactus'),
    path("products/<int:id>/",views.products,name='products'),
    path("payment",views.payment,name='payment'),
    path("order",views.order,name='order'),
    path("tracker",views.tracker,name='tracker'),
    path("passwordchange",views.passwordchange,name='passwordchange') 
]


