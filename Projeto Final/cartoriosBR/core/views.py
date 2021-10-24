from core.models import Cartorios
from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import *
from django.shortcuts import render, HttpResponse, redirect

class CartoriosViewSet(viewsets.ModelViewSet):
    """
    Retorna lista de cartórios paginadas de 50 em 50
    """
    queryset = Cartorios.objects.all()
    serializer_class = CartoriosSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.

# def retorna_uf(request,text_uf):
#     uf = Cartorios.objects.get(uf=text_uf)
#     return uf


# class CartoriosUfViewSet(request,viewsets.ModelViewSet):
#     """
#     Retorna a lista de cartórios da UF paginadas de 50 em 50
#     """
#     uf = self.object.uf
#     self.object.timein = self.request.POST.get("uf", "")
#
#     queryset = Cartorios.objects.all().filter(uf=uf)
#     serializer_class = CartoriosSerializer
#     permission_classes = [permissions.IsAuthenticated]