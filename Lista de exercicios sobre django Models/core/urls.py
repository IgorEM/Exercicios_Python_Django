from django.urls import path

from .views import people_list, people_create

app_name = 'core'

urlpatterns = [
    path('list/', people_list, name="lista"),
    path('create/', people_create, name="criar"),
]
