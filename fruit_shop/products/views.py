from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Home, Signup, Login, Comment, Order, Load


def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home': home})

# /products -> index
# Uniform Resource Locator (URL or address)
def index(request):
    product = Product.objects.all()
    return render(request, 'index.html',{'products':product})


def new(request):
    return HttpResponse("New Products")

def signup(request):
    signup = Signup.objects.all()
    return render(request, 'signup.html', {'signup': signup})

def login(request):
    login = Login.objects.all()
    return render(request, 'login.html', {'login': login})

def comment(request):
    comment = Comment.objects.all()
    return render(request, 'comment.html', {'comment': comment})

def order(request):
    order = Order.objects.all()
    return render(request, 'order.html', {'order': order})

def load(request):
    load = Load.objects.all()
    return render(request, 'load.html', {'load': load})

