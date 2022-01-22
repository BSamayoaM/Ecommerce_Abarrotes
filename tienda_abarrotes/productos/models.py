from django.db import models


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
    cantidad = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.producto.nombre} x {self.cantidad}"
class Mermas(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.producto.nombre} x {self.cantidad}"
class Modelos(models.Model):
    nombre = models.Charfield(max_length=50)
    def __str__(self):
        f"{self.nombre}"
class Marcas(models.Model):
    nombre = models.Charfield(max_length=50)
    def __str__(self):
        f"{self.nombre}"
class Categorias(models.Model):
    nombre = models.Charfield(max_length=50)
    def __str__(self):
        f"{self.nombre}"
class Fotos_Productos(models.Model):
    ruta = models.Charfield(max_length=250)
    producto = models.ForeignKey(Productos,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.ruta}"
