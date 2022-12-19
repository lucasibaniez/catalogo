from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from utils.mixins import IsAdminMixin

from .forms import ProductoForm
from .models import Producto, MeGusta

"""
def admin_listado_productos(request):
    template_name = "productos/listado.html"

    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, template_name, contexto)
"""

class AdminListadoProductos(LoginRequiredMixin, IsAdminMixin, ListView):
    template_name = "productos/listado.html"
    model = Producto
    context_object_name = "productos"
    paginate_by = 20

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre_producto = self.request.GET.get("buscador")
        if nombre_producto:
            productos = productos.filter(nombre__contains=nombre_producto)

        return productos.order_by("nombre")


class NuevoProducto(CreateView):
    model = Producto 
    template_name = "productos/nuevo_producto.html"
    form_class = ProductoForm

    def get_success_url(self):
        return reverse("productos:admin_listado_productos")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["producto"] = Producto.objects.get(id=3) 
        return context
    
    """ 
    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoProducto, self).form_valid()
    """


class EditarProducto(UpdateView):   
    model = Producto 
    template_name = "productos/editar.html"
    form_class = ProductoForm     

    def get_success_url(self):
        return reverse("productos:admin_listado_productos")


def dar_me_gusta(request, id_producto):
    mg = MeGusta.objects.filter(usuario=request.user, producto__id=id_producto)
    if not mg:
        mg = MeGusta.objects.create(usuario=request.user, producto=Producto.objects.get(id=id_producto))
    return HttpResponseRedirect(reverse("inicio"))

