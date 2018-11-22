from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o nome do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Usuário',
            }
        )
    )
    email = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a marca do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }
        )
    )
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com a descrição do produto.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )

    password1 = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com sua senha.'},
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Senha',
            }
        )
    )
    password2 = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com sua senha.'},
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Senha',
                'name' : 'Password',
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmar Senha"
        self.fields['name'].label = "Nome"

class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o username desejado.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Usuário',
            }
        )
    )
    email = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com o email do usuário.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
            }
        )
    )
    name = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com seu nome.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Nome',
            }
        )
    )
    password = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório! Preencha este campo com sua senha.'},
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Senha',
            }
        )
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'name', 'password']
