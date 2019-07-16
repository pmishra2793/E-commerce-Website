from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all()
    print (products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slide':nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def tracker(request):
    return render(request,'tracker.html')

def search(request):
    return render(request,'search.html')

def productview(request):
    return render(request,'productview.html')

def checkout(request):
    return render(request,'checkout.html')


