from django.contrib import admin
from .models import Categoria, Cliente, Pratos, Pedido, Funcionario, Cesta

@admin.register(Categoria)
@admin.register(Cliente)
@admin.register(Pratos)
@admin.register(Pedido)
@admin.register(Funcionario)
@admin.register(Cesta)

class Categoria(admin.ModelAdmin):
    pass

