from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from .models import Pratos, Funcionario, Pedido, Cliente, Categoria, Cesta
from .forms import Cadastrar_Pratos_Form, Cadastrar_Cliente_Form


def lista_pratos(request):
    if request.user.is_authenticated:
        lista= Pratos.objects.all()

        if Funcionario.objects.filter(usuario= request.user):
            return render(request, 'app_delivery/lista_pratos.html', {'lista': lista})

        if Cliente.objects.filter(usuarios= request.user):
            return render(request, 'app_delivery/lista_pratos_cliente.html', {'lista': lista})
        
        else:
            return redirect('cadastrar_cliente')
    else:
        return render(request, 'app_delivery/erro.html')

def excluir_prato(request, id):
    if request.user.is_authenticated:
            prato = Pratos.objects.get(pk=id)
            prato.delete()
            return redirect(reverse('lista_de_pratos'))
    else:
        redirect('/autenticacao/login')

class cadastrar_pratos(FormView):
    template_name= 'app_delivery/cadastrar_prato_form.html'
    form_class= Cadastrar_Pratos_Form

    def form_valid(self, form):
        dados = form.clean()
        prato = Pratos(nome= dados['nome'], descricao= dados['descricao'],
                        preco= dados['preco'] , categoria= dados['categoria'])

        prato.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('lista_de_pratos')

##########################################################################################


class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'app_delivery/register.html'

class cadastrar_cliente(FormView):
    template_name= 'app_delivery/cadastrar_cliente_form.html'
    form_class= Cadastrar_Cliente_Form

    def form_valid(self, form):
        dados = form.clean()
        cliente = Cliente(cpf= dados['cpf'], nome= dados['nome'], cep=dados['cep'], 
                    logradouro= dados['logradouro'], complemento= dados['complemento'], 
                    usuarios= self.request.user)

        cliente.save()
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse('sucesso')

class SucessoView(TemplateView):
    template_name = 'app_delivery/cadastro_sucesso.html'

##########################################################################################

def add_cesta(request, id):
    if request.user.is_authenticated:
        clientes= Cliente.objects.get(usuarios= request.user)
        if Cesta.objects.filter(cliente= clientes):
            cesta= Cesta.objects.get(cliente__usuarios=request.user)
            prato= Pratos.objects.get(pk= id)
            cesta.lista.append(Pratos.objects.get(pk= id))
            cesta.save()

        else:
            cesta= Cesta()
            cesta.cliente= clientes
            prato= Pratos.objects.get(pk= id)
            cesta.lista.append(Pratos.objects.get(pk= id))
            cesta.save()
        
        return redirect('lista_de_pratos')

        
    else:
        redirect('/autenticacao/login')


def finalizar_pedido(request):
    if request.user.is_authenticated:
        pedido= Pedido()
        clientes= Cliente.objects.get(usuarios= request.user)
        cesta= Cesta.objects.get(cliente= clientes)
        pedido.cliente= clientes
        pedido.status= 'Processando'
        
        
        for i in cesta.lista:
            pedido.listaPratos.append(i)

        cesta.lista=[]
        cesta.save()
        pedido.save()
        pedido.listaPratos=[]        
        
        listaP= Pedido.objects.filter(cliente= clientes)


        return redirect('lista_de_pratos')

    else:
        return render(request, 'app_delivery/erro.html')
        
        

def ver_pedidos(request):
    if request.user.is_authenticated:
        cliente= Cliente.objects.get(usuarios= request.user)
        lista_pedido= Pedido.objects.filter(cliente= cliente)
        
        return render(request, 'app_delivery/lista_pedido_cliente.html', {'lista_pedido': lista_pedido})
    else:
        return render(request, 'app_delivery/erro.html')


##########################################################################################

def pedidos_nao_atendidos(request):
    if request.user.is_authenticated:
        if Funcionario.objects.filter(usuario= request.user):
            lista = Pedido.objects.filter(concluido= False)

            return render(request, 'app_delivery/pedidos_nao_atendidos.html', {'lista': lista})
    else:
        return render(request, 'app_delivery/erro.html')
        
def aceita_pedido(request, id):
    if request.user.is_authenticated:
        pedido = Pedido.objects.get(pk=id)
        pedido.aceitar= True
        pedido.status= "Em produção"
        pedido.save()
        return redirect(reverse('pedidos'))
    else:
        redirect('/autenticacao/login')

def pedido_pronto(request, id):
    if request.user.is_authenticated:
        pedido = Pedido.objects.get(pk=id)
        pedido.concluido= True
        pedido.status= "Saiu para entrega"
        pedido.save()
        return redirect(reverse('pedidos'))
    else:
        redirect('/autenticacao/login')


            

