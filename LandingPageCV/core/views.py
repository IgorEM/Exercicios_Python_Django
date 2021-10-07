from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

def hello(request):
    return render(request, "core/hello.html") #templates tá lá no settings