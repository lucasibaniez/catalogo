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

    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, template_name, contexto)

"""
def login(request):
    if 'btn_ingresar'in request.GET:
        username = request.GET.get("username")
    
    return render(request, "login.html", {})    
"""    