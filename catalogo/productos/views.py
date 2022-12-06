from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto

def admin_listado_productos(request):
    template_name = "productos/listado.html"

    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, template_name, contexto)


class NuevoProducto(CreateView):
    model = Producto 
    template_name = "productos/nuevo_producto.html"
    form_class = ProductoForm

    def get_success_url(self):
        return reverse("productos:admin_listado_productos")