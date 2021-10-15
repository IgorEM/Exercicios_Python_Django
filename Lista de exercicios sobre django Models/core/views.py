from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import InserePessoaForm
from django.http import HttpResponseRedirect

from core.models import People


def people_list(request):
    pessoas = People.objects.all()
    context = {
        "pessoas": pessoas
    }
    return render(request, 'core/list2.html', context=context)


def people_create(request):

    if request.method == 'POST':
        form = InserePessoaForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = InserePessoaForm()

    return render(request, 'core/create.html', context={'form': form})
