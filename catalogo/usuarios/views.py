from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import UsuarioForm
from .models import Usuario

class Registro(CreateView):
    model = Usuario 
    template_name = "usuarios/registro.html"
    form_class = UsuarioForm

    def get_success_url(self):
        return reverse("login")
