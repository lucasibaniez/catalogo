from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()

    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre