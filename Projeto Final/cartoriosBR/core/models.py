from django.db import models


# Create your models here.
class Cartorios(models.Model):
    cnpj = models.CharField(max_length=18)
    cns = models.CharField(max_length=8)
    data_de_instalacao = models.CharField(max_length=10)
    nome_oficial = models.CharField(max_length=300)
    nome_fantasia = models.CharField(max_length=300, null=True, blank=True)
    nome_do_titular = models.CharField(max_length=100)
    nome_do_substituto = models.CharField(max_length=100)
    nome_do_juiz = models.CharField(max_length=100)
    observacao = models.CharField(max_length=300)
    ultima_atualizacao = models.CharField(max_length=300)
    horario_de_funcionamento = models.CharField(max_length=300)
    area_de_abrangencia = models.CharField(max_length=300)
    atribuicoes = models.CharField(max_length=300)
    comarca = models.CharField(max_length=300)
    entrancia = models.CharField(max_length=300)


class Adressess(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )

    endereco = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    cep = models.CharField(max_length=8, null=True)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)



class ContactInformation(models.Model):
    homepage = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=17)
    fax = models.CharField(max_length=100)


"""
Lendo o arquivo csv com pandas:

python manage.py shell
import pandas as pd
df = pd.read_csv('Cartorios_utf8.csv', sep=';', index_col=False, na_values="", skipinitialspace=True)

o que cada parametro faz :

index_col=False: Crie um indice numerico ao invés de assumir a primeira coluna "UF" como indice.
na_values="": Para valores "", salve NaN
skipinitialspace=True: Ignore espaços vazios repetidos. POr exemplo "       ", vira "" ou "    nada     " vira "nada"

"""