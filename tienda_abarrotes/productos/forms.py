from django.forms import ModelForm
from . import models

class ProductosForm(ModelForm):
    class Meta:
        model=models.Productos
        fields=('nombre','descripcion','existencia','precio_compra',
                'precio_venta'
                ,'stock','proveedor','categoria',)
class DescuentosForm(ModelForm):
    class Meta:
        model=models.Descuentos
        fields = ('cantidad','fecha_inicio','fecha_fin','producto',)
class MermasForm(ModelForm):
    class Meta:
        model=models.Mermas
        fields = ('fecha','cantidad','producto')
class ModelosForm(ModelForm):
    class Meta:
        model=models.Modelos
        fields = ('nombre',)
class MarcasForm(ModelForm):
    class Meta:
        model=models.Marcas
        fields = ('nombre',)
class CategoriasForm(ModelForm):
    class Meta:
        model=models.Categorias
        fields = ('nombre',)
class Fotos_ProductosForm(ModelForm):
    class Meta:
        model=models.Fotos_Productos
        fields = ('ruta','producto')
