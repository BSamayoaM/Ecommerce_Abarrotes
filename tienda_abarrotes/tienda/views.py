from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import models


def inicio(request):
    pass
class PaisesList(ListView):
    model=models.Paises
class PaisesDetail(DetailView):
    model=models.Paises
class PaisesCreate(CreateView):
    model=models.Paises
class PaisesUpdate(UpdateView):
    model=models.Paises
class PaisesDelete(DeleteView):
    model=models.Paises


class EntidadesList(ListView):
    model=models.Entidades
class EntidadesDetail(DetailView):
    model=models.Entidades
class EntidadesCreate(CreateView):
    model=models.Entidades
class EntidadesUpdate(UpdateView):
    model=models.Entidades
class EntidadesDelete(DeleteView):
    model=models.Entidades


class MunicipiosList(ListView):
    model=models.Municipios
class MunicipiosDetail(DetailView):
    model=models.Municipios
class MunicipiosCreate(CreateView):
    model=models.Municipios
class MunicipiosUpdate(UpdateView):
    model=models.Municipios
class MunicipiosDelete(DeleteView):
    model=models.Municipios
