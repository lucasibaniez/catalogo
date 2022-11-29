from django.shortcuts import render

from productos.models import Producto

def inicio(request):
    template_name = "index.html"
    
    # ===============================
    # query en django utilizando el orm
    """
    p = Producto.objects.create(
        nombre="Pantalon",
        precio=2000,
        descripcion="Pantalon azul"
    )
    """
    productos = Producto.objects.all()

    contexto = {
        'productos': productos
    }
    return render(request, template_name, contexto)