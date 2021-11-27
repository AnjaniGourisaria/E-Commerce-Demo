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


def profile(request):
   
    def login(request):
            if request.method == 'POST':
                usernamelog = request.POST['usernamelog']
                passwordlog = request.POST['passwordlog']
                user = auth.authenticate(usernamelog=usernamelog, passwordlog=passwordlog)

                if user is not None:
                    auth.login(request, user)
                    return redirect('login')
                else:
                    messages.error(request, "Credentials Invalid")
                    return redirect('profile')
            else:
                return render(request, 'profile.html')
            
            
    def create_ac(request):
            if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                reppassword = request.POST['reppassword']
                if password == reppassword:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, "Email Exist in database")
                        return redirect('profile')
                    elif User.objects.filter(username=username).exists():
                        messages.error(request, "Username Exist in database")
                        return redirect('profile')
                    else:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save()
                        return redirect('profile')
                else:
                    messages.error(request, "Password Not same Matched")
                    return redirect('profile')
            else:
                return render(request, 'profile.html')
            
            
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            login(request)
        elif request.POST.get('submit') == 'sign_up':
            create_ac(request)
    else:
        return render(request, 'profile.html')
    
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
