from django import forms
from django.forms import ModelForm
from .models import Market


class MarketForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )
    photo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Url da foto',
            }
        )
    )
    class Meta:
        model = Market
        fields = ['name', 'photo']


class SortOptionForm(forms.Form):
    OPTIONS = [
        ('default', 'Ordenar por:'),
        ('nomeAz', 'Nome A-Z'),
        ('nomeZa', 'Nome Z-A'),
        ('avaliacaoMelhores', "Melhores avaliados"),
        ('avaliacaoPiores', 'Piores avaliados'),
    ]
    choice = forms.ChoiceField(choices=OPTIONS)
