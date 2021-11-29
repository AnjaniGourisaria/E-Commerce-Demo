from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

def sign_in(request):
    return render(request,'sign_in.html')

def sign_up(request):
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            reppassword = request.POST['reppassword']
            print("usernmae",username)
            print("enail",email)
            print("password",password)
            print("repassword",reppassword)
            
        else:
            return render(request, 'sign_up.html')
            

    
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
