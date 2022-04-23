from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def products(request):
    queryset = Product.objects.all()
    return render(request, 'products.html', {'products': queryset})

def promotions(request):
    return render(request, 'promotions.html')