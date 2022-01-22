from django.forms import ModelForm
from . import models

class PaisesForm(ModelForm):
    model=models.Paises
    fields = '__all__'
class MunicipiosForm(ModelForm):
    model=models.Municipios
    fields = '__all__'
class EntidadesForm(ModelForm):
    model=models.Entidades
    fields = '__all__'
