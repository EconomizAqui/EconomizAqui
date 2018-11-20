from django.shortcuts import render
from .models import Product
from .models import Historic
from .forms import ProductForm
from .forms import HistoricForm
from django.shortcuts import redirect

def base(request):
    return render(request, 'base.html')

def view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {"product": product})

def list_products(request):
    products = Product.objects.all()
    for historico in products.last().historic.all():
        print("PREÇO", historico.price)
    return render(request, 'products.html', {"products": products})

def create_product(request):
    form_product = ProductForm(request.POST or None)
    form_historic = HistoricForm(request.POST or None)
    if form_product.is_valid() and form_historic.is_valid():
        form_historic.save()
        historico = Historic.objects.last()
        product = form_product.save()
        print("Historico", historico)
        product.historic.add(historico)
        product.save()
        return render(request,  "productCreate.html", {"form_product": form_product, "form_historic": form_historic, "method": "Criar", "alert": "Produto criado com sucesso"})
    else:
        return render(request, 'productCreate.html', {"form_product": form_product, "form_historic": form_historic, "method": "Criar"})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form_product = ProductForm(request.POST or None, instance=product)
    if form_product.is_valid():
        form_product.save()
        return render(request, 'productCreate.html', {"form_product": form_product, "method": "Atualizar", "alert": "Produto atualizado com sucesso"})
    else:
        return render(request, 'productCreate.html', {"form_product": form_product, "method": "Atualizar"})

def new_price(request, id):
    product = Product.objects.get(id=id)
    form_historic = HistoricForm(request.POST or None)
    if form_historic.is_valid():
        form_historic.save()
        historico = Historic.objects.last()
        product.historic.add(historico)
        product.save()
        return render(request, 'productCreate.html', {"form_historic": form_historic, "method": "Adicionar Preço para", "alert": "Preço foi alterado com sucesso"})
    else:
        return render(request, 'productCreate.html', {"form_historic": form_historic, "method": "Adionar Preço para"})


def delete_product(request):
    return render(request, 'delete_product.html')
