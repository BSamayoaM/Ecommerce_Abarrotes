from django.forms import ModelForm
from . import models

class UsuariosForm(ModelForm):
    model=models.Usuarios
    fields = '__all__'
class ComentariosForm(ModelForm):
    model=models.Comentarios
    fields = ('comentario',)
class CalificacionesForm(ModelForm):
    model=models.Calificaciones
    fields = ('calificacion',)
class Tipos_UsuariosForm(ModelForm):
    model=models.Tipos_Usuarios
    fields = '__all__'
