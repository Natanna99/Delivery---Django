from django.contrib import admin
from django.urls import path, include
from .views import lista_pratos, excluir_prato, cadastrar_pratos, cadastrar_cliente, register, pedidos_nao_atendidos
from .views import aceita_pedido, pedido_pronto, add_cesta, SucessoView, ver_pedidos, finalizar_pedido

urlpatterns = [
    path('lista_pratos/', lista_pratos, name= 'lista_de_pratos'),
    path('delete/<int:id>/', excluir_prato, name='excluir_prato'),
    path('cadastrar_pratos/', cadastrar_pratos.as_view(), name='cadastrar_pratos'),

    path('cadastrar_cliente/', cadastrar_cliente.as_view(), name='cadastrar_cliente'),
    path('cadastrar/', register.as_view(), name='cadastrar'),
    path('sucesso/', SucessoView.as_view(), name='sucesso'),

    path('add_cesta/<int:id>/', add_cesta, name= 'add_cesta'),
    path('finalizar_pedido', finalizar_pedido, name= 'finalizar_pedido'),
    path('ver_pedidos', ver_pedidos, name= 'ver_pedidos' ),

    path('pedidos/', pedidos_nao_atendidos, name='pedidos'),
    path('aceita_pedido/<int:id>', aceita_pedido, name='aceita_pedido'),
    path('pedido_pronto/<int:id>', pedido_pronto, name='pedido_pronto'),

]