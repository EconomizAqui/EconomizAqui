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

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return render(request, 'productCreate.html', {"form": form, "method": "Atualizar"})
    else:
        return render(request, 'productCreate.html', {"form": form, "method": "Atualizar"})

def delete_product(request):
    return render(request, 'delete_product.html')
