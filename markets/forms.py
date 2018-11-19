from django import forms
from django.forms import ModelForm
from .models import Market


class MarketForm(ModelForm):
    class Meta:
        model = Market
        fields = ['name']


class SortOptionForm(forms.Form):
    OPTIONS = [
        ('default', 'Ordenar por:'),
        ('nomeaz', 'Nome A-Z'),
        ('nomeza', 'Nome Z-A'),
        ('avaliacaomelhores', "Melhores avaliados"),
        ('avaliacaopiores', 'Piores avaliados'),
    ]
    choice = forms.ChoiceField(choices=OPTIONS)
