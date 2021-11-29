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
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path("jewellery",views.jewellery,name='jewellery'),
    path("fashion",views.fashion,name='fashion'),
    path("electronic",views.electronic,name='electronic'),
    path("seacrh",views.search,name='search'),
    path("addcart",views.addcart,name='addcart'),
    path("sign_up",views.sign_up,name='sign_up'),
    path("shop",views.shop,name='shop'),
    path("checkout",views.checkout,name='checkout'),
    path("login",views.login,name='login'),
    path("sign_in",views.sign_in,name='sign_in'),
    
]


