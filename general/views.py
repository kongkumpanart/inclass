from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"homepage.html")

def category(request):
    return render(request,"category.html")

def product(request):
    return render(request,"product.html")

def checkout(request):
    return render(request,"checkout.html")

def contact(request):
    return render(request,"contact.html")