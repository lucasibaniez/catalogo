from django.db import models

from categorias.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()

    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, related_name="categorias")

    categoria2 = models.ManyToManyField(Categoria)

    # ficha = models.OneToOneField(Ficha)

    def __str__(self):
        return self.nombre


x = Producto.objects.filter(id=1).first() # exists()
if x:
    pass

"""
class ProductoCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    # fecha
"""