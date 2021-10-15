import pandas as pd
from django.core.management.base import BaseCommand

from core.models import People


class Command(BaseCommand):

    help = 'Load people data from CSV file'

    def handle(self, *args, **kwargs):
        if People.objects.exists():
            print("A tabela de pessoas já foi populada. Nada a fazer.")
        else:
            df = pd.read_csv('people_data.csv')
            df['sexo'] = df.sexo.apply(
                lambda k: "F" if k == "Feminino" else "M"
            )
            data = df.to_dict('records')

            objs = People.objects.bulk_create([People(**item) for item in data])

            print(f"{len(objs)} pessoas inseridas")
