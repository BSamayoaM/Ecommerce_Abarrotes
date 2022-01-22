from django.db import models

class Paises(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        f"{self.nombre}"
class Entidades(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.Foreignkey(Paises,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.nombre}"
class Municipios(models.Model):
    nombre = models.CharField(max_length=100)
    entidad = models.Foreignkey(Entidades,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.nombre}"


