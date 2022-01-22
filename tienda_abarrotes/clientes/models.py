from django.db import models


class Ventas(models.Model):
    fecha   = models.DateField()
    subtotal  = models.FloatField()
    iva  = models.FloatField()
    total  = models.FloatField()
    usuario  = models.ForeignKey()
    def __str__(self):
        f"{self.fecha} {self.usuario}"
