from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    pais=models.ForeignKey(Paises,on_delete=models.CASCADE)
    entidad=models.ForeignKey(Entidades,on_delete=models.CASCADE)
    municipio=models.ForeignKey(Municipios,on_delete=models.CASCADE)
    tipo_usuario=models.ForeignKey(Tipos_Usuarios,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
class Comentarios(models.Model):
    comentario = models.CharField(max_length=1000)
    fecha = models.DateField()
    usuario =models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.comentario} --- {self.usuario}"
class Calificaciones(models.Model):
    calificacion = models.IntegerField()
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    def __str__(self):
        f"{self.calificacion} --- {self.usuario}"
class Tipos_Usuarios(models.Model):
    nombre  = models.CharField(max_length=80)
    nivel  = models.IntegerField()
    def __str__(self):
        f"{self.nombre} --- {self.nivel}"
