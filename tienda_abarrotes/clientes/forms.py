from django.forms import ModelForm
from . import models

class VentasForm(ModelForm):
    class Meta:
        model=models.Ventas
        fields=('fecha','subtotal','iva','total',)
