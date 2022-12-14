from django.db import models

from categorias.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()

    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre