from django.core.management.base import BaseCommand
from core.models import ContactInformation
import pandas as pd


class Command(BaseCommand):
    help = 'Carrega as informaçoes de contato do arquivo csv'

    def handle(self, *args, **kwargs):
        if ContactInformation.objects.exists():#se existir
            print("A tabela de core_contactinformation já foi populada. Nada a fazer.")
        else:
            df = pd.read_csv('Cartorios_utf8.csv', sep=';', index_col=False, na_values="", skipinitialspace=True,
                             usecols=["homepage","email","telefone","fax"])

            data = df.to_dict('records')

            #criando uma coleçao de objetos:
            colecao_infcontatos = [ContactInformation(**item) for item in data]

            infcont_objs = ContactInformation.objects.bulk_create(colecao_infcontatos, batch_size=1000)
            print(f"{len(infcont_objs)} informações de contatos inseridas")