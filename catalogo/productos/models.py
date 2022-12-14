from django.db import models

from categorias.models import Categoria
from usuarios.models import Usuario

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()

    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, related_name="categorias", blank=True)

    categoria2 = models.ManyToManyField(Categoria)

    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    # models.FileField
    # models.BinaryField

    # ficha = models.OneToOneField(Ficha)

    def __str__(self):
        return self.nombre


class MeGusta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

"""
class ProductoCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    # fecha
"""