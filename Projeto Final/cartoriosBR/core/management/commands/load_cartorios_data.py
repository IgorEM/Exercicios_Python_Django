from django.core.management.base import BaseCommand
from core.models import Cartorios
import pandas as pd


class Command(BaseCommand):
    help = 'Carrega os dados de Cartorios do arquivo csv'

    def handle(self, *args, **kwargs):
        if Cartorios.objects.exists():#se existir
            print("A tabela de core_cartorios já foi populada. Nada a fazer.")
        else:
            df = pd.read_csv('Cartorios_utf8.csv', sep=';', index_col=False, na_values="", skipinitialspace=True,
                             usecols=["cnpj","cns","data_de_instalacao","nome_oficial","nome_fantasia",
                                      "nome_do_titular","nome_do_substituto","nome_do_juiz","observacao",
                                      "ultima_atualizacao","horario_de_funcionamento","area_de_abrangencia",
                                      "atribuicoes","comarca","entrancia"])

            data = df.to_dict('records')

            #criando uma coleçao de objetos:
            colecao_cartorios = [Cartorios(**item) for item in data]

            cart_objs = Cartorios.objects.bulk_create(colecao_cartorios, batch_size=1000)
            print(f"{len(cart_objs)} cartorios inseridos")