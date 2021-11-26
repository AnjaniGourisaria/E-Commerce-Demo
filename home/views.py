from django.shortcuts import render ,HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is done suessfully")
def fashion(request):
    return render(request,'fashion.html')
def jewellery(request):
    return render(request,'jewellery.html')
def electronic(request):
    return render(request,'electronic.html')
def addcart(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'addcart.html')
def profile(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'profile.html')
def search(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'search.html')
def shop(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'shop.html')
def checkout(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'checkout.html')
def login(request):
    #return HttpResponse("this is done suessfully")
    return render(request,'login.html')
