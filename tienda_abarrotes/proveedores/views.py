from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import models


class ProveedoresList(ListView):
    model=models.Proveedores
class ProveedoresDetail(DetailView):
    model=models.Proveedores
class ProveedoresCreation(CreateView):
    model=models.Proveedores
class ProveedoresUpdate(UpdateView):
    model=models.Proveedores
class ProveedoresDelete(DeleteView):
    model=models.Proveedores


class ComprasList(ListView):
    model=models.Compras
class ComprasDetail(DetailView):
    model=models.Compras
class ComprasCreation(CreateView):
    model=models.Compras
class ComprasUpdate(UpdateView):
    model=models.Compras
class ComprasDelete(DeleteView):
    model=models.Compras
