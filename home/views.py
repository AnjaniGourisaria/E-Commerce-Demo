from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .models import Contacts, Details #, SignUp
import re


# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is done suessfully")


def fashion(request):
    return render(request, 'fashion.html')


def jewellery(request):
    return render(request, 'jewellery.html')


def electronic(request):
    return render(request, 'electronic.html')


def addcart(request):
    # return HttpResponse("this is done suessfully")
    return render(request, 'addcart.html')


def sign_up(request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            reppassword = request.POST['reppassword']
            # print("username",username)
            # print("email",email)
            # print("password",password)
            # print("repassword",reppassword)
            if password == reppassword:
                if User.objects.filter(email=email).exists():
                    messages.error(request ,"Email Exist in database")
                    return redirect('sign_up')
                elif username.isalpha and len(username)>5 and User.objects.filter(username=username).exists():
                    messages.error(request ,"Username Exist in database and it should be in letter only and username>5")
                    return redirect('sign_up')
                elif len(password)<8:
                     messages.error(request ,"bigger password near 8+")
                     return redirect('sign_up')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save();
                    return redirect('sign_in')       
            else:
                messages.error(request ,"Password not matched")
                return redirect('sign_up')
        else:
            return render(request, 'sign_up.html')
    
def sign_in(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        print(password)
        user = authenticate(request, username=username,password=password)
        
        if user is not None:
            print('logined')
            auth_login(request, user)
            messages.success(request,'Login Sucessfully')
            return redirect('/')
        else:
            messages.error(request,'Invailed credentials')
            return redirect('sign_in')
    else:
        return render(request, 'sign_in.html')

    
 # return HttpResponse("this is done suessfully")


def search(request):
    # return HttpResponse("this is done suessfully")
    return render(request, 'search.html')


def shop(request):
    # return HttpResponse("this is done suessfully")
    return render(request, 'shop.html')


def checkout(request):
    # return HttpResponse("this is done suessfully")
    return render(request, 'checkout.html')


def login(request):
    return HttpResponse("this is done suessfully")
    # if request.method == 'POST':
    # else:
    #     HttpResponse('404 Not Found')
def log_out(request):
        logout(request)
        return redirect('/')
def contactus(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # print(uname,email,phone,msg)
        if not (len(uname) == 0) and not uname.isalpha:
            messages.error(request,'Please Fill the Username Correctly Only Letter')
            print("[+]Debug: check uname ",uname,email,phone,msg)
        elif not (len(email) == 0) and not (re.fullmatch(regex, email)):
            messages.error(request,'Please Fill the Username Correctly Only Email')
            print("[+]Debug: check email ",uname,email,phone,msg)
        elif not (len(phone) == 0) and not len(phone)<=10:
            messages.error(request,'Please Fill the Phone Correctly Only Numbers')
            print("[+]Debug: check phone ",uname,email,phone,msg)
        else:
            user= Contacts(username=uname,email=email,phone=phone,msg=msg)
            messages.error(request,'Sussesfully Submitted the form')
            print("[+]Debug: check all ",uname,email,phone,msg)
            user.save()
    return render(request, 'contactus.html')