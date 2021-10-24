from core.models import Cartorios,Adressess
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import *
from django.shortcuts import render, HttpResponse, redirect
import json

class CartoriosViewSet(viewsets.ModelViewSet):
    """
    Retorna lista de cartórios paginadas de 50 em 50
    """
    queryset = Cartorios.objects.all()
    serializer_class = CartoriosSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdressesViewSet(viewsets.ModelViewSet):
    """
    Retorna lista de endereços paginadas de 50 em 50
    """
    queryset = Adressess.objects.all()
    serializer_class = AdressessSerializer
    permission_classes = [permissions.IsAuthenticated]

def lista_cartorios(request):
    cartorios = Cartorios.objects.all().values('nome_oficial','cnpj','atribuicoes','uf')
    dados = {'cartorios': cartorios}
    return render(request, 'cartorios.html',dados)

def lista_cartorios_uf(request,text_uf):
    cartorios = Cartorios.objects.all().filter(uf=text_uf).values('nome_oficial','cnpj','uf','id')
    dados = {'cartorios': cartorios}
    return render(request, 'cartoriosuf.html', dados)

def lista_cartorios_id(request,text_uf,text_id):
    cartorios = Cartorios.objects.all().filter(uf=text_uf).filter(id=text_id)\
        .values("id","uf","cnpj","cns","data_de_instalacao","nome_oficial","nome_fantasia","nome_do_titular","nome_do_substituto","nome_do_juiz","observacao","ultima_atualizacao","horario_de_funcionamento","area_de_abrangencia","atribuicoes","comarca","entrancia")
    dados = {'cartorios': cartorios}
    return render(request, 'cartoriosid.html', dados)

def lista_cartorios_id1(request,text_id):
    cartorios = Cartorios.objects.all().filter(id=text_id)\
        .values("id","uf","cnpj","cns","data_de_instalacao","nome_oficial","nome_fantasia","nome_do_titular","nome_do_substituto","nome_do_juiz","observacao","ultima_atualizacao","horario_de_funcionamento","area_de_abrangencia","atribuicoes","comarca","entrancia")
    dados = {'cartorios': cartorios}
    return render(request, 'cartoriosid1.html', dados)
