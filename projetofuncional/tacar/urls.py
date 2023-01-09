"""tacar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(),name='url_registrar'),
    path('', home, name='url_principal'),
    path('cadastro_cliente/', cadastro_cliente, name='Cadastro-cliente'),
    path('cadastro_veiculo/', cadastro_veiculo, name='Cadastro-veiculo'),
    path('cadastro_fabricante/', cadastro_fabricante, name='cadastro-fabricante'),
    path('lista_veiculos/', lista_veiculos, name='Lista-veiculos'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('lista_clientes/', lista_clientes, name='Lista-clientes'),
    path('lista_fabricante/', lista_fabricante, name='Lista-fabricante'),
    path('tabela/', lista_tabela, name='tabela-precos'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('excluir_cliente/<int:id>/', excluir_cliente, name='url_excluir_cliente'),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name="url_exclui_veiculo"),
    path('cadastro_rotativos/', cadastro_rotativo, name="url_cadastro_rotativo"),
    path('lista_rotativos/', listagem_rotativo, name="url_lista_rotativo"),
    path('altera_rotativo/<int:id>/', altera_rotativo, name="url_altera_rotativo"),
    path('lista_tabela/',lista_tabela, name='url_lista_tabela'),
    path('cadastro_mensalistas/', cadastro_mensalistas, name='url_cadastro_mensalistas'),
    path('lista_mensalistas/', lista_mensalistas, name='url_lista_mensalistas'),
    path('alterar_mensalista/<int:id>/', alterar_mensalista, name='url_alterar_mensalista'),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media1/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]