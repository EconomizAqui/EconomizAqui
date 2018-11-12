from django.shortcuts import render, redirect, get_object_or_404
from markets.models import Market
from .forms import MarketForm


def market_list(request, template_name='market_list.html'):
    markets = Market.objects.all()
    return render(request, template_name, {'markets': markets})

def market_view(request, pk, template_name='market_detail.html'):
    market = get_object_or_404(Market, pk=pk)    
    return render(request, template_name, {'object':market})

def market_create(request, template_name='market_form.html'):
    form = MarketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('market_list')
    return render(request, template_name, {'form':form})

def market_update(request, pk, template_name='market_form.html'):
    market = get_object_or_404(Market, pk=pk)
    form = MarketForm(request.POST or None, instance=market)
    if form.is_valid():
        form.save()
        return redirect('market_list')
    return render(request, template_name, {'form':form})

def market_delete(request, pk, template_name='market_confirm_delete.html'):
    market = get_object_or_404(Market, pk=pk)    
    if request.method=='POST':
        market.delete()
        return redirect('market_list')
    return render(request, template_name, {'object':market})