from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.Charfield(max_length=50)
    descripcion = models.TextField()
    existencia = models.IntegerField()
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    def __str__(self):
        f"{self.nombre}"
class Descuentos(models.Model):
    pass
    def __str__(self):
        pass
class Mermas(models.Model):
    pass
    def __str__(self):
        pass
class Modelos(models.Model):
    pass
    def __str__(self):
        pass
class Marcas(models.Model):
    pass
    def __str__(self):
        pass
class Categorias(models.Model):
    pass
    def __str__(self):
        pass
class Fotos_Productos(models.Model):
    pass
    def __str__(self):
        pass
