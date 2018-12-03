from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Product
from .models import Historic
from .models import ShoppingList
from markets.models import Market
from .forms import ProductForm
from .forms import HistoricForm
from django.shortcuts import redirect
import simplejson as json

def base(request):
    return render(request, 'base.html')

def view(request, id):
    product = Product.objects.get(id=id)
    historic_price = []
    historic_commerce = []
    if request.POST:
        historic = product.historic.last()
        historic.points += int(request.POST['points'])
        historic.save()

    point = False
    for historic in product.historic.all():
        price = json.dumps(historic.price)
        historic_price.append(price)
        historic_commerce.append(historic.commerce.name)

    historic_price = json.dumps(historic_price)
    historic_commerce = json.dumps(historic_commerce)

    return render(request, 'product.html', {"product": product, "historic_price": historic_price, "historic_commerce": historic_commerce})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products": products})

def create_product(request):
    form_product = ProductForm(request.POST or None)
    form_historic = HistoricForm(request.POST or None, data=request.POST or None)
    if form_product.is_valid() and form_historic.is_valid():
        commerce = Market.objects.all().get(id = request.POST['cod_commerce'])
        historico = Historic.objects.create(price = request.POST['price'], commerce = commerce)
        historico.save()
        product = form_product.save()
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
    form_historic = HistoricForm(request.POST or None, data=request.POST or None)
    if form_historic.is_valid():
        commerce = Market.objects.all().get(id = request.POST['cod_commerce'])
        historico = Historic.objects.create(price = request.POST['price'], commerce = commerce)
        historico.save()
        product.historic.add(historico)
        product.save()
        return render(request, 'productCreate.html', {"form_historic": form_historic, "method": "Adicionar Preço para", "alert": "Preço foi alterado com sucesso"})
    else:
        return render(request, 'productCreate.html', {"form_historic": form_historic, "method": "Adionar Preço para"})


def delete_product(request):
    return render(request, 'delete_product.html')

def shopping_list(request):
    shopping_list = ShoppingList.objects.get(user=request.user) 
    
    product_list = shopping_list.products.all()

    total_price = 0
    total_price = sum(product.historic.last().price for product in product_list)

    return render(
        request,
        'shopping_list.html',
        {'shopping_list': shopping_list, 'product_list': product_list, 'total_price': total_price}
        )

def add_product_list(request,id):
    shopping_list = ShoppingList.objects.get(user=request.user)
    
    product = Product.objects.get(id=id)
    shopping_list.products.add(product)

    return HttpResponseRedirect(reverse('shopping_list'))

def remove_product_list(request,id):
    shopping_list = ShoppingList.objects.get(user=request.user)
    
    product = Product.objects.get(id=id)
    shopping_list.products.remove(product)

    return HttpResponseRedirect(reverse('shopping_list'))