from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})
