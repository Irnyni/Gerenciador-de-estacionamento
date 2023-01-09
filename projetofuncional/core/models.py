from distutils.command.upload import upload
from email.policy import default
from optparse import BadOptionError
from tabnanny import verbose
from django.db import models
from math import trunc, ceil, floor

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='media1/fotos_clientes', blank=True, null=True)

    class MyModel(models.Model):
        upload = models.ImageField(upload_to='media1/')
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'


class Fabricante(models.Model):
    descricao = models.CharField(max_length=100, verbose_name= "Fabricante")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'Fabricantes'


class Veiculo(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField(default=2022, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='media1/fotos_veiculos', blank=True, null=True)


    def __str__(self):
        return f'{self.placa} ({self.modelo})'

    class Meta:
        verbose_name_plural = 'Veiculos'


class Tabela(models.Model):
    descricao = models.CharField(max_length=50,verbose_name= "Descrição")
    valor = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return f'{self.descricao} - ({self.valor})'

    class Meta:
        verbose_name_plural = 'Tabelas'


class Rotativo(models.Model):
    id_Veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name= "Veiculo")
    id_Tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name= "Tarifa")
    data_entrada = models.DateTimeField(auto_now=False, auto_now_add= False,verbose_name="Entrada")
    data_saida = models.DateTimeField(auto_now=False, auto_now_add= False,blank=True, null=True,verbose_name="Saída")
    pago = models.BooleanField (default=False, blank=True, null=True, verbose_name= "Pago")
    total = models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=2,verbose_name="Total a pagar")
    def __str__(self):
        return f'{self.id_Veiculo} - ({self.data_entrada})'

    class Meta:
        verbose_name_plural = 'Rotativos'

    def calcula_total(self):
        if self.data_saida:
            horas = (self.data_saida - self.data_entrada).total_seconds() / 3600
            obj = Tabela.objects.get(id=self.id_Tabela.pk)
            adicional = 0.60 * float(obj.valor) * 0.60
            taxa=0.0
            if horas <= 0.5:
                taxa = float(obj.valor) / 2.0
            else:
                tolerancia = (horas) - trunc(horas)
                if tolerancia <= 0.25:
                    taxa = float(obj.valor) + (floor(horas - 1)) * adicional
                else:
                    taxa = float(obj.valor) + (ceil(horas - 1)) * adicional

            self.total = taxa
            return True
        else:
            return False


class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=30,verbose_name="Tipo de pagamento")


    def __str__(self):
         return self.descricao


    class Meta:
        verbose_name_plural = 'FormaPagamentos'

class Mensalista(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    id_Tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name= "Tarifa")
    dia_vencimento = models.IntegerField(default=5, verbose_name= "Dia de vencimento")
    em_pendencia = models.BooleanField(default=False, blank=True, null=True, verbose_name= "Devedor")
    forma_pagamento = models.ForeignKey(FormaPagamento,blank=True, null=True,on_delete=models.CASCADE,verbose_name="Forma de pagamento")
    total = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True, verbose_name="Valor")

    def __str__(self):
        return f'(str(self.id_cliente)-({self.id_Tabela}))'
    class Meta:
        verbose_name_plural = 'Mensalistas'

    def calculo_desconto(self):
         obj= FormaPagamento.objects.get(id=self.forma_pagamento.pk)
         obj2 = Tabela.objects.get(id=self.id_Tabela.pk)
         if obj.descricao == 'DINHEIRO':
            total= obj2.valor * 0.95
         elif obj.descricao == 'PIX':
            total=obj2.valor * 0.93
         else:
             total=obj2

         self.total = total
         return total


