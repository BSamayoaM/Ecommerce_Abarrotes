from django.shortcuts import render
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class ProductosList(ListView):
    model=models.Productos
class ProductosDetail(DetailView):
    model=models.Productos
class ProductosCreation(CreateView):
    model=models.Productos
class ProductosUpdate(UpdateView):
    model=models.Productos
class ProductosDelete(DeleteView):
    model=models.Productos

class DescuentosList(ListView):
    model=models.Descuentos
class DescuentosDetail(DetailView):
    model=models.Descuentos
class DescuentosCreation(CreateView):
    model=models.Descuentos
class DescuentosUpdate(UpdateView):
    model=models.Descuentos
class DescuentosDelete(DeleteView):
    model=models.Descuentos

class MermasList(ListView):
    model=models.Mermas
class MermasDetail(DetailView):
    model=models.Mermas
class MermasCreation(CreateView):
    model=models.Mermas
class MermasUpdate(UpdateView):
    model=models.Mermas
class MermasDelete(DeleteView):
    model=models.Mermas

class ModelosList(ListView):
    model=models.Modelos
class ModelosDetail(DetailView):
    model=models.Modelos
class ModelosCreation(CreateView):
    model=models.Modelos
class ModelosUpdate(UpdateView):
    model=models.Modelos
class ModelosDelete(DeleteView):
    model=models.Modelos

class MarcasList(ListView):
    model=models.Marcas
class MarcasDetail(DetailView):
    model=models.Marcas
class MarcasCreation(CreateView):
    model=models.Marcas
class MarcasUpdate(UpdateView):
    model=models.Marcas
class MarcasDelete(DeleteView):
    model=models.Marcas

class CategoriasList(ListView):
    model=models.Categorias
class CategoriasDetail(DetailView):
    model=models.Categorias
class CategoriasCreation(CreateView):
    model=models.Categorias
class CategoriasUpdate(UpdateView):
    model=models.Categorias
class CategoriasDelete(DeleteView):
    model=models.Categorias

class Fotos_ProductosList(ListView):
    model=models.Fotos_Productos
class Fotos_ProductosDetail(DetailView):
    model=models.Fotos_Productos
class Fotos_ProductosCreation(CreateView):
    model=models.Fotos_Productos
class Fotos_ProductosUpdate(UpdateView):
    model=models.Fotos_Productos
class Fotos_ProductosDelete(DeleteView):
    model=models.Fotos_Productos
