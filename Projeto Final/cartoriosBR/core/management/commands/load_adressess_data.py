from django.core.management.base import BaseCommand
from core.models import Adressess
import pandas as pd
# from django.db import DatabaseError,transaction
# https://docs.djangoproject.com/en/3.2/topics/db/transactions/

class Command(BaseCommand):
    help = 'Carrega os dados de Endereços do arquivo csv'

    def handle(self, *args, **kwargs):
        if Adressess.objects.exists():#se existir
            print("A tabela de core_adressess já foi populada. Nada a fazer.")
        else:
            df = pd.read_csv('Cartorios_utf8.csv', sep=';', index_col=False, na_values="", skipinitialspace=True,usecols=["endereco","bairro","municipio","cep","uf"])

            data = df.to_dict('records') #pega cada linha do dataframe e transforma num dicionario.

            #criando uma coleçao de objetos:
            #enderecos = [Adressess(**item) for item in data]
            #29/09 1:03:55
            end_objs = Adressess.objects.bulk_create([Adressess(**item) for item in data], batch_size=1000)
            print(f"{len(end_objs)} endereços inseridos")

            """  ----------------------------COMENTARIOS RELEVANTES-----------------------------------
            
            In:  data[0] 
            Out: 
            {'uf': 'AC',
            'endereco': 'Av. Governador Edmundo Pinto, 581',
            'bairro': 'Centro',
            'municipio': 'Acrelândia',
            'cep': 69945000.0}
            """


            """ 
            Isso aqui é lento, 
            
            for item in data:
                Adressess.objects.create(**item)
                
            pq ta abrindo uma conexao no banco de dados, 
            fazendo um insert pra cada item.
            UMA FORMA DE MELHORAR ISSO É USAR O bulck_create que recebe uma coleção de objetos
            
            
                Robson Fernandes:
                
                "O create recebe uma lista de nomeados.
                Vc poderia passar foo=bar, foo2=bar2, foo3=bar3 OU **{"foo": "bar", "foo2": "bar2", "foo3": "bar3",}"
                
            """