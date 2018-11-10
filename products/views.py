from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.shortcuts import redirect

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,  "products.html")
    else:
        return render(request, 'productCreate.html', {"form": form, "method": "Criar"})
