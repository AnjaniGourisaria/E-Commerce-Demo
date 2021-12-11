from typing import Reversible
from django.http.response import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .models import (Product , Contacts , Customer , Cart , OrderPlaced)
import re
from .forms import CustomerRegistrationForm
import time

# Create your views here.


# class ProductView(View):
#     def get(self,request):
#         p = Product.objects.filter(sub_category='Phone')
#         return render(request, 'index.html',{'p':p})

# def fashion(request):
#     return render(request, 'fashion.html')


# def jewellery(request):
#     return render(request, 'jewellery.html')


# def electronic(request):
#     return render(request, 'electronic.html')


# def sign_up(request):
#         if request.method == 'POST':
#             username = request.POST['username']
#             email = request.POST['email']
#             password = request.POST['password']
#             reppassword = request.POST['reppassword']
#             # print("username",username)
#             # print("email",email)
#             # print("password",password)
#             # print("repassword",reppassword)
#             if password == reppassword:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request ,"Email Exist in database")
#                     return redirect('sign_up')
#                 elif username.isalpha and len(username)>5 and User.objects.filter(username=username).exists():
#                     messages.error(request ,"Username Exist in database and it should be in letter only and username>5")
#                     return redirect('sign_up')
#                 elif len(password)<8:
#                      messages.error(request ,"bigger password near 8+")
#                      return redirect('sign_up')
#                 else:
#                     user = User.objects.create_user(username=username,email=email,password=password)
#                     user.save();
#                     return redirect('sign_in')       
#             else:
#                 messages.error(request ,"Password not matched")
#                 return redirect('sign_up')
#         else:
#             return render(request, 'sign_up.html')


PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )

def get_client_ip(request):
    """get the client ip from the request
    """
    remote_address = request.META.get('REMOTE_ADDR')
    # set the default value of the ip to be the REMOTE_ADDR if available
    # else None
    ip = remote_address
    # try to get the first non-proxy ip (not a private ip) from the
    # HTTP_X_FORWARDED_FOR
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        # remove the private ips from the beginning
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        # take the first ip which is not a private one (of a proxy)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip

def index(request):
    ip = get_client_ip(request)
    p = Product.objects.filter(sub_category='Phone')
    now = int(time.strftime('%H'))   
    return render(request, 'index.html',{'p':p,'now':now})
    # return HttpResponse("this is done suessfully")


def addcart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    if product_id:
        product = Product.objects.get(id=product_id)
        u=Cart(user=user, product=product)
        u.save()
        #return update_cart(product)
    else:
        return redirect('/cart')
    
# update cart for quantity update
def  update_cart(request, product):
    quantity = request.GET.get('quantity')
    update=Cart(user=request.user,product=product)
    update.save()
            


def sync_cart(request):
    if request.user.is_authenticated:
        product=Cart.objects.filter(user=request.user)
        
        return render(request, 'addcart.html',{'products':product})
    else:
        redirect('sign_up')
           
        

def sign_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        # if not (len(username) == 0) and not (len(password) == 0) and not username.isalpha(): # working but the create user with (username='1+1+1') with this they cant login due to not username.isaplha
        #     fail2=True
        #     return render(request,'sign_in.html',{'fail2':fail2})     
        # else:
        user = authenticate(request, username=username,password=password)
        if user is not None:
            print('logined')
            auth_login(request, user)
            messages.success(request,'Login Sucessfully')
            return redirect('/')
        else:
            fail=True
            messages.error(request,'Invailed credentials')
            return render(request,'sign_in.html',{'fail':fail})     
    else:
        return render(request, 'sign_in.html')
        #return HttpResponse("this is done suessfully")
        
        
        

class CustumerRegestrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'sign_up.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
        else:
            return render(request, 'sign_up.html',{'form':form})
        
        
        
        
def search(request):
    # return HttpResponse("this is done suessfully")
    product_name = request.POST['searching']
    print(product_name)
    Apple = Product.objects.filter(product_name__contains=product_name)
    return render(request, 'search.html',{'Apple':Apple}) 





def shop(request):    
    # return HttpResponse("this is done suessfully")
    now = int(time.strftime('%H'))  
    return render(request, 'shop.html',{'now':now})
   
        

def checkout(request):
    # return HttpResponse("this is done suessfully")
    return render(request, 'checkout.html')

def about(request):
    pass


def help(request):
    pass



def login(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user
            name = request.POST['name']
            name2 = request.POST['name2']
            phone = request.POST['phone']
            station = request.POST['station']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            zip = request.POST['zip']
            regex = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            regex2 = r'[A-Za-z0-9!@#()_-]{5,15}'
            name=name+" "+name2
            # print(name,name2,station,phone,address,city,state,zip)
            sign = Customer(user=username,name=name,phone=phone,station=station,locality=address,city=city,state=state,zipcode=zip)
            sign.save()
            loginform = Customer.objects.filter(user=request.user) 
            print("hello")
            ip = get_client_ip(request)
            now = int(time.strftime('%H'))  
            return render(request, 'login.html',{'loginform':loginform,'now':now}) 
        else:
            loginform = Customer.objects.filter(user=request.user) 
            print("hello")
            ip = get_client_ip(request)
            now = int(time.strftime('%H'))  
            return render(request, 'login.html',{'loginform':loginform,'now':now}) 
            #return render(request, 'login.html') 
    else:
        return redirect('sign_up')


   
   
def log_out(request):
        logout(request)
        return redirect('/')


    
    
def contactus(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        regex = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        regex2 = r'[A-Za-z0-9!@#()_-]{5,15}'
        # print(uname,email,phone,msg)
        if not (len(uname) == 0) and not (re.fullmatch(regex2, uname)):
            messages.error(request,'Please Fill the Username Correctly Only Letter')
            unameerr=True
            # print("[+]Debug: check uname ",uname,email,phone,msg)
            print("[+]Debug: contact us", uname,email,phone,msg)
            return render(request, 'contactus.html',{'usererr':unameerr})
        elif not (len(email) == 0) and not (re.fullmatch(regex, email)):
            messages.error(request,'Please Fill the Email Correctly Only Email')
            # print("[+]Debug: check email ",uname,email,phone,msg)
            emailerr=True
            return render(request, 'contactus.html',{'emailerr':emailerr})  
        elif not (len(phone) == 0) and not len(phone)<=10 and not int(phone): 
            messages.error(request,'Please Fill the Phone Correctly Only Numbers')
            # print("[+]Debug: check phone ",uname,email,phone,msg)
            phoneerr=True
            return render(request, 'contactus.html',{'phoneerr':phoneerr})
        else:
            ip = get_client_ip(request)
            user= Contacts(username=uname,email=email,phone=phone,msg=msg)
            user.save()
            fullsuscess=True
            messages.error(request,'Sussesfully Submitted the form')
            return render(request, 'contactus.html',{'fullsuscess':fullsuscess}) 
            # print("[+]Debug: check all ",uname,email,phone,msg)   
    else:
        return render(request, 'contactus.html',{'notpost':"it was not post method "})
    



    
def products(request,id):
    p = Product.objects.filter(id=id)
    return render(request, 'products.html',{'p':p})



    
def order(request):
        return render(request, 'order.html')


    

def tracker(request):
        return render(request, 'tracker.html')
    




def passwordchange(request):
    return render(request, 'passwordchange.html')
 