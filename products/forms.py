from django import forms
from .models import Product
from .models import Historic

class HistoricForm (forms.ModelForm):
    price = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o preço do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Preço',
            }
        )
    )
    commerce = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o comércio do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Comércio',
            }
        )
    )
    class Meta:
        model = Historic
        fields = ['price', 'commerce']


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o nome do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )
    brand = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a marca do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Marca',
            }
        )
    )
    description = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Descrição',
            }
        )
    )
    category = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a categoria do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Categoria',
            }
        )
    )
    photo = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a url da imagem do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Url da foto',
            }
        )
    )
    class Meta:
        model = Product
        fields = ['name', 'brand', 'description', 'category', 'photo']
