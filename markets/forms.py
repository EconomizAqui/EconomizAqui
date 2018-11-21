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
        ('nomeAz', 'Nome A-Z'),
        ('nomeZa', 'Nome Z-A'),
        ('avaliacaoMelhores', "Melhores avaliados"),
        ('avaliacaoPiores', 'Piores avaliados'),
    ]
    choice = forms.ChoiceField(choices=OPTIONS)
