from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Contact
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print (products)
    # params = {'no_of_slide':nSlides,'range':range(1,nSlides),'product':products}
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    # allProds = [[nSlides,range(1,nSlides),products],
    #             [nSlides,range(1,nSlides),products]]
    params = {'allProds':allProds}
    return render(request,'index.html',params)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        mobile = request.POST.get('mobile','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,mobile=mobile,desc=desc)
        contact.save()
    return render(request,'contact.html')

def tracker(request):
    return render(request,'tracker.html')

def search(request):
    return render(request,'search.html')

def productview(request,id):
    product = Product.objects.filter(id = id)
    print (product)
    params = {'product':product[0]}
    return render(request,'productview.html',params)

def checkout(request):
    return render(request,'checkout.html')


