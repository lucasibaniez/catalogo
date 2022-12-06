from django.shortcuts import render

from productos.models import Producto

def admin_listado_productos(request):
    template_name = "productos/listado.html"

    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, template_name, contexto)