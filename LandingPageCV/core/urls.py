from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #/core
    path('hello', views.hello), #/core/hello
]