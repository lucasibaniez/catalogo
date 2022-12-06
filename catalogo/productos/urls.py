from django.urls import path

from . import views

app_name="productos"

urlpatterns = [
    path('admin/listado/', views.admin_listado_productos, name="admin_listado_productos"),
]