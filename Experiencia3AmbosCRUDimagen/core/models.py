from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=100, verbose_name='Nombre Producto')
    descripcionProducto = models.CharField(max_length=1000, verbose_name='Descripcion Producto')
    precioProducto = models.CharField(max_length=10, verbose_name='Precio')
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
            return self.nombreProducto

class Cliente(models.Model):
    correoCliente = models.CharField(primary_key=True,max_length=50, verbose_name='Correo Electronico')
    nombreCliente = models.CharField(max_length=200, verbose_name='Nombre Cliente')
    contraseñaCliente = models.CharField(max_length=200, default="*********")
    nacionalidadCliente = models.CharField(max_length=50, verbose_name='Nacionalidad Cliente')
    sexoCliente = models.CharField(max_length=10, verbose_name='Sexo Cliente')
    fechaCliente = models.DateField(verbose_name='Fecha de Nacimiento')
    telefonoCliente = models.IntegerField(verbose_name='Telefono Cliente')

    def __str__(self):
            return self.nombreCliente