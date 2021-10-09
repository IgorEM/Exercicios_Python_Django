from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def home(request):
    return render(request, "core/home.html") #templates tá lá no settings