from django.forms import ModelForm
from . import models

class ProveedoresForm(ModelForm):
    class Meta:
        model = models.Proveedores
        fields = '__all__'
class ComprasForm(ModelForm):
    class Meta:
        model = models.Compras
        fields = '__all__'
