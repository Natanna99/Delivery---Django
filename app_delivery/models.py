from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome= models.CharField(max_length= 30, blank= True, null= True)

    def __str__(self):
        return self.nome


class Pratos(models.Model):
    nome= models.CharField(max_length= 50, blank= True, null= True)
    descricao= models.TextField()
    preco= models.FloatField()
    #imagem= models.FileField(upload_to = 'imagens/' , max_length = 100, blank= True, null= True ) 
    categoria= models.ForeignKey(Categoria, on_delete= models.CASCADE, blank= True, null= True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.preco)

class Cliente(models.Model):
    cpf= models.CharField(max_length= 11, blank= True, null= True)
    nome= models.CharField(max_length= 50, blank= True, null= True)
    cep= models.CharField(max_length= 250, blank=True, null= True)
    logradouro= models.CharField(max_length= 250, blank=True, null= True)
    complemento= models.CharField(max_length= 250, blank=True, null= True)
    usuarios= models.ForeignKey(User, on_delete= models.CASCADE, blank= True, null= True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.logradouro)

class Funcionario(models.Model):
    cargo= models.CharField(max_length= 10, blank= True, null= True)
    nome= models.CharField(max_length= 50, blank= True, null= True)
    usuario= models.ForeignKey(User, on_delete= models.CASCADE, blank= True, null= True)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.cargo)

class Cesta(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete= models.CASCADE, blank= True, null= True)
    lista= []


class Pedido(models.Model):
    listaPratos=[]
    pratos= models.ForeignKey(Cesta, on_delete= models.CASCADE, blank= True, null= True)
    cliente= models.ForeignKey(Cliente, on_delete= models.CASCADE, blank= True, null= True)
    status= models.CharField(max_length= 20, blank= True, null= True)
    aceitar= models.BooleanField(default=False)
    concluido= models.BooleanField(default= False)

    def __str__(self):
        return self.cliente.nome


