from django.shortcuts import redirect, render
from core.forms import *
from core.models import Cliente, Fabricante, Veiculo,Tabela
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'core/index.html')

class Registrar (generic.CreateView):
     form_class = UserCreationForm
     success_url = '/'
     template_name = "registration/register.html"


def cadastro_cliente(request):

    try:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            form.save()
            messages.success(request, f'Cliente  { nome }  cadastrado com sucesso!')
            return redirect('Lista-clientes')
        contexto = {'form': form, 'titulo': 'Cadastro de Cliente','stringbotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)



def lista_clientes(request):

    try:
        dados = Cliente.objects.all()
        if request.POST:
            if request.POST['pesquisa']:
              dados = Cliente.objects.filter(nome=request.POST['pesquisa'])

        contexto = {'dados': dados}
        return render(request, 'core/lista_clientes.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def cadastro_veiculo(request):

    try:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo': 'Cadastro de Veiculo','stringbotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def lista_veiculos(request):
    try:
        dados = Veiculo.objects.all()
        if request.POST:
            if request.POST ['pesquisa']:
                dados=Veiculo.objects.filter(placa=request.POST['pesquisa'])

        contexto = {'dados': dados}
        return render(request, 'core/lista_veiculos.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def cadastro_fabricante(request):
    try:
        form = FormFabricante(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'titulo': 'Cadastro de Fabricante','stringbotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def lista_fabricante(request):
    try:
        dados = Fabricante.objects.all()
        if request.POST:
            if request.POST ['pesquisa']:
                dados=Fabricante.objects.filter(descricao=request.POST[ 'pesquisa' ])
        contexto = {'dados': dados}
        return render(request, 'core/lista_fabricantes.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def altera_cliente(request,id):
     try:
         objeto= Cliente.objects.get(id=id)
         form = FormCliente( request.POST or None, request.FILES or None, instance=objeto )
         if form.is_valid():

             nome = form.cleaned_data ['nome']
             form.save()
             messages.success(request,f'Dados do cliente { nome } atualizado com sucesso!')
             return redirect('Lista-clientes')
         contexto = {'form': form, 'titulo': 'Atualizar Cliente','stringbotao': 'Atualizar'}
         return render(request,'core/cadastro.html',contexto)
     except Exception as mensagem_erro:
         contexto = {'msg_erro': mensagem_erro}
         return render(request, '500.html', contexto)

def excluir_cliente(request,id):
     try:
         object = Cliente.objects.get(id=id)
         if request.POST:
             object.delete()
             return redirect('Lista-clientes')
         contexto = {'url':'/lista_clientes/','objeto': object.nome}
         return render(request,'core/confirma_exclusao.html',contexto)
     except Exception as mensagem_erro:
         contexto = {'msg_erro': mensagem_erro}
         return render(request, '500.html', contexto)

def exclui_veiculo(request, id):
    try:
        objeto = Veiculo.objects.get(id=id)
        if request.POST:
            objeto.delete()
            return redirect('url_lista_veiculos')
        contexto = {'url': '/lista_veiculos/', 'objeto': objeto.modelo}
        return render(request, 'core/confirma_exclusao.html', contexto)

    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def tabela_preco(request):
    return render(request, 'core/tabela.html')


def cadastro_rotativo(request):
    try:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_rotativos')
        contexto = {'form': form, 'titulo': 'Cadastro de rotativo', 'stringbotao':'Cadastrar','calendario':True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)

def listagem_rotativo(request):
    try:
        dados = Rotativo.objects.all()
        if request.POST:
            if request.POST ['pesquisa']:
                dados=Rotativo.objects.filter(descricao=int(request.POST[ 'pesquisa' ]))
        contexto = {'dados': dados}
        return render(request, 'core/lista_rotativos.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)

def altera_rotativo(request, id):
    try:
        objeto = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=objeto)

        if form.is_valid():
            objeto.calcula_total()
            form.save()
            return redirect('url_lista_rotativo')

        contexto = {'form': form, 'titulo': 'Atualização de rotativo', 'stringbotao': 'Atualizar','calendario':True}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)

def lista_tabela(request):
    try:
        dados = Tabela.objects.all()
        if request.POST:
            if request.POST ['pesquisa']:
                dados=Tabela.objects.filter(descricao=request.POST[ 'pesquisa' ])
        contexto = {'dados': dados}
        return render (request, 'core/tabela.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def cadastro_mensalistas(request):
    try:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalistas')
        contexto = {'form': form, 'titulo': 'Cadastro de mensalista', 'stringbotao': 'Cadastrar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def lista_mensalistas(request):
    try:
        dados= Mensalista.objects.all()
        if request.POST:
            if request.POST ['pesquisa']:
                dados=Mensalista.objects.filter(descricao=request.POST[ 'pesquisa' ])
        contexto= {'dados':dados}
        return render (request, 'core/lista_mensalistas.html',contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)
def alterar_mensalista(request, id):
    try:
        objeto = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('url_lista_mensalistas')
        contexto = {'form': form, 'titulo': 'Atualizar Mensalista', 'stringbotao': 'Atualizar'}
        return render(request, 'core/cadastro.html', contexto)
    except Exception as mensagem_erro:
     contexto={ 'msg_erro': mensagem_erro}
     return render(request, '500.html',contexto)

def altera_veiculo(request, id):
    objeto = Veiculo.objects.get(id=id)
    form = FormVeiculo(request.POST or None, request.FILES or None, instance=objeto)
    if form.is_valid():
        form.save()
        contexto = {'objeto': objeto.placa, 'url': '/lista_veiculos/'}
        return render(request, 'core/mensagem_salvo.html', contexto)
    contexto = {'form': form, 'titulo': 'Atualiza Veiculo',
                'stringbotao': 'Salvar'}
    return render(request, 'core/cadastro.html', contexto)

