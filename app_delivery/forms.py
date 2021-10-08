from django import forms
from .models import Pratos, Pedido, Cliente, Funcionario, Categoria
from django.contrib.auth.forms import UserCreationForm


class Cadastrar_Pratos_Form(forms.Form):
    nome= forms.CharField(max_length=128, min_length=4)
    descricao= forms.CharField(max_length=128, min_length= 10)
    preco= forms.FloatField()
    categoria= forms.ModelChoiceField(queryset= Categoria.objects.all())
    #imagem= forms.FileField()

    def clean(self):
        dados = super().clean()
        return dados

class Cadastrar_Cliente_Form(forms.Form):
    cpf= forms.CharField(max_length= 11,  min_length=11 )
    nome= forms.CharField(max_length= 50,  min_length=4)
    logradouro= forms.CharField(max_length= 250, min_length=4 )
    cep= forms.CharField(max_length= 250, min_length=4 )
    complemento= forms.CharField(max_length= 250, min_length=4)


    def clean(self):
        dados = super().clean()
        return dados