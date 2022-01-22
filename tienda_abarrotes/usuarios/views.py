from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import models

class UsuariosList(ListView):
    model=models.Proveedores
class UsuariosDetail(DetailView):
    model=models.Proveedores
class UsuariosCreate(CreateView):
    model=models.Proveedores
class UsuariosUpdate(UpdateView):
    model=models.Proveedores
class UsuariosDelete(DeleteView):
    model=models.Proveedores


class ComentariosList(ListView):
    model=models.Proveedores
class ComentariosDetail(DetailView):
    model=models.Proveedores
class ComentariosCreation(CreateView):
    model=models.Proveedores
class ComentariosUpdate(UpdateView):
    model=models.Proveedores
class ComentariosDelete(DeleteView):
    model=models.Proveedores


class CalificacionesList(ListView):
    model=models.Calificaciones
class CalificacionesDetail(DetailView):
    model=models.Calificaciones
class CalificacionesCreate(CreateView):
    model=models.Calificaciones
class CalificacionesUpdate(UpdateView):
    model=models.Calificaciones
class CalificacionesDelete(DeleteView):
    model=models.Calificaciones


class Tipos_UsuariosList(ListView):
    model=models.Tipos_Usuarios
class Tipos_UsuariosDetail(DetailView):
    model=models.Tipos_Usuarios
class Tipos_UsuariosCreate(CreateView):
    model=models.Tipos_Usuarios
class Tipos_UsuariosUpdate(UpdateView):
    model=models.Tipos_Usuarios
class Tipos_UsuariosDelete(DeleteView):
    model=models.Tipos_Usuarios
