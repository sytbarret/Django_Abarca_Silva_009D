from django.urls import path
from .views import Inicio, Registro, Galeria, Somos, Contacto, calculadora, apiMonedas, MostrarProducto, CrearProducto, ModificarProducto,EliminarProducto, MostrarCliente, CrearCliente, ModificarCliente, EliminarCliente


urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('Registro/', Registro, name="Registro" ),
    path('Galeria/', Galeria, name="Galeria"),
    path('Somos/', Somos, name="Somos"),
    path('Contacto/', Contacto, name="Contacto"),
    path('calculadora/', calculadora, name="calculadora"),
    path('apiMonedas/', apiMonedas, name="apiMonedas"),
    path('MostrarProducto/', MostrarProducto, name="MostrarProducto"),
    path('CrearProducto/', CrearProducto, name="CrearProducto"),
    path('ModificarProducto/<id>', ModificarProducto, name="ModificarProducto"),
    path('EliminarProducto/<id>', EliminarProducto, name="EliminarProducto"),
    path('MostrarCliente/', MostrarCliente, name="MostrarCliente"),
    path('CrearCliente/', CrearCliente, name="CrearCliente"),
    path('ModificarCliente/<id>', ModificarCliente, name="ModificarCliente"),
    path('EliminarCliente/<id>', EliminarCliente, name="EliminarCliente"),
]

