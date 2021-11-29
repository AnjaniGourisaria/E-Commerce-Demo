from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
#from .models import Feature

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
            print("username",username)
            print("email",email)
            print("password",password)
            print("repassword",reppassword)
            if password == reppassword:
                if User.objects.filter(email=email).exists():
                    messages.error(request ,"Email Exist in database")
                    return redirect('sign_up')
                elif len(username)>5 and User.objects.filter(username=username).exists():
                    messages.error(request ,"Username Exist in database")
                    return redirect('sign_up')
                elif len(password)<8:
                     messages.error(request ,"bigger password near 8+")
                     return redirect('sign_up')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save();
                    return redirect('login')       
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
        return render(request,'sign_in.html')

    
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
    # return HttpResponse("this is done suessfully")
    return render(request, 'login.html')
