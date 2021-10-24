from core.models import Cartorios, Adressess
from rest_framework import serializers


class CartoriosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cartorios
        fields = [
                'cnpj',
                'cns',
                'data_de_instalacao',
                'nome_oficial',
                'nome_fantasia',
                'nome_do_titular',
                'nome_do_substituto',
                'nome_do_juiz',
                'observacao',
                'ultima_atualizacao',
                'horario_de_funcionamento',
                'area_de_abrangencia',
                'atribuicoes',
                'comarca',
                'entrancia',
                'uf']

class AdressessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adressess
        fields = '__all__'