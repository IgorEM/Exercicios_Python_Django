from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #/core
    path('home', views.home), #/core/home
]