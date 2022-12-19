from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from productos.models import Producto

from utils.mixins import is_admin_required

@is_admin_required()
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

    contexto = {
        'productos': Producto.objects.filter(activo=True)
    }
    return render(request, template_name, contexto)

"""
def login(request):
    if 'btn_ingresar'in request.GET:
        username = request.GET.get("username")
    
    return render(request, "login.html", {})    
"""    