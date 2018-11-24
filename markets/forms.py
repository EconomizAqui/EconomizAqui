from django import forms
from django.forms import ModelForm
from .models import Market


class MarketForm(ModelForm):
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o nome do mercado.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )
    photo = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a url da imagem do mercado.'},
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
        ('nomeAz', 'Nome A-Z'),
        ('nomeZa', 'Nome Z-A'),
        ('avaliacaoMelhores', "Melhores avaliados"),
        ('avaliacaoPiores', 'Piores avaliados'),
    ]
    choice = forms.ChoiceField(
            choices=OPTIONS,
                    widget=forms.Select(
                        attrs={
                            'onselect': 'AumentaPontos(this)',
                            'class': 'form-control'
                        }
                    )
            )
