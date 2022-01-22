from django.db import models

class Proveedores(models.Model):
    nombre  =models.CharField(max_length=50)
    rfc =models.CharField(max_length=50)
    razon_social =models.CharField(max_length=50)
    contacto =models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    telefono =models.IntegerField()
    pais =models.ForeignKey(Paises,on_delete=models.CASCADE)
    entidad =models.ForeignKey(Entidades,on_delete=models.CASCADE)
    municipio =models.ForeignKey(Municipios,on_delete=models.CASCADE)
    direccion =models.CharField(max_length=50)
    cp =models.CharField(max_length=50)
    colonia =models.CharField(max_length=50)
    def __str__(self):
        f"{self.nombre} --- {self.razon_social}"
class Compras(models.Model):
    fecha= models.DateField()
    subtotal= models.FloatField()
    iva= models.FloatField()
    total= models.FloatField()
    proveedor= models.ForeignKey(Proveedores,on_delete=models.CASCADE)
    usuarios= models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.proveedor} --- {self.fecha} --- {self.total}"
