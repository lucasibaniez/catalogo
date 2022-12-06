from django.urls import path

from . import views

app_name="productos"

urlpatterns = [
    path('admin/listado/', views.admin_listado_productos, name="admin_listado_productos"),
    path('admin/nuevo/', views.NuevoProducto.as_view(), name="admin_nuevo_producto"),
]