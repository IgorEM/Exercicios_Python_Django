from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date
import json
#iexact na frente independete maiusculo ou menusculo

class PeopleManager(models.Manager):

    def first_five_people(self):
        return self.model.objects.order_by('nome')[:5]

    def starts_with(self, text):
        return self.model.objects.filter(nome__istartswith=text)

    def para_json(self, ids):
        return self.model.objects.filter(id=ids).values()

    def contem(self, text):
        return self.model.objects.filter(nome__icontains=text)

    def to_json(self, ids):
        data = self.model.objects.filter(id=ids).values()
        data = data[0] #para exibir em formato json
        data['data_nasc'] = data['data_nasc'].isoformat() #type str
        data['altura'] = str(data['altura']) #type str
        return json.dumps(data) #tranforma objetos python em

class People(models.Model):

    GENDER_CHOICES = [
        ("F", "Feminino"), #(banco de dados, Usuario enxerga)
        ("M", "Masculino"),
    ]

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=15)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mae = models.CharField(max_length=150)
    pai = models.CharField(max_length=150)
    celular = models.CharField(max_length=150)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.PositiveIntegerField()
    tipo_sanguineo = models.CharField(max_length=10)
    endereco = models.CharField(max_length=10, null=True)
    cidade = models.CharField(max_length=10, null=True)
    estado = models.CharField(max_length=10, null=True)
    cep = models.CharField(max_length=10, null=True)
    pais = models.CharField(max_length=10, null=True)
    """
    1. Permitir entrada de dados nulo
    2. Gerar uma migração vazia, e escrever a lógica para popular essa coluna
        nos registros existentes.
    3. Forçar que um valor seja informado para o campo recém criado.
    """

    objects = PeopleManager()

    @property
    def idade(self):
        data_atual = date.today()
        idade = relativedelta(data_atual, self.data_nasc).years
        return idade

    def __str__(self):
        return f"{self.nome} - {self.data_nasc} - {self.idade} anos de idade " #alterando o __str__ da class People
