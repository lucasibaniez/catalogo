# catalogo
Sitio de catalogos de productos, desarrollado el Informatorio - Comision 3 (2022)

metodo 1:
Para levantar el proyecto, hay que crear un arhivo .env al mismo nivel del settings con las siguiente estructura:
NAME=ssssssssss
USER=ssssssssss
PASSWORD=ssssssssss
HOST=ssssssssss

metodo 2:
Crear el archivo local.py al mismo nivel que base.py en settings, con la siguiente estructura (catalogo/catalogo/settings):
#####################################################################
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': "catalogo",
        'USER': "sa",
        'PASSWORD': "P741852963",
        'HOST': "localhost",
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        },
    }
}
#####################################################################   