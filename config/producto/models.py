from django.db import models


# Create your models here.
class Fabrica(models.Model):
    nombre = models.CharField(max_length=255)
    pais = models.CharField(max_length=50, blank=True, null=True)

    # producto = models.ManyToManyField(Producto)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=255)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    # fabrica = models.OneToOneField(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    # fabrica = models.ManyToManyField(Fabrica)
