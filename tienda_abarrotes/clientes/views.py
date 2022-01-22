from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import models

class VentasList(ListView):
    model=models.Ventas
class VentasDetail(DetailView):
    model=models.Ventas
class VentasCreation(CreateView):
    model=models.Ventas
class VentasUpdate(UpdateView):
    model=models.Ventas
class VentasDelete(DeleteView):
    model=models.Ventas
