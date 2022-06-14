from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Producto, Cliente


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['idProducto', 'nombreProducto', 'descripcionProducto', 'precioProducto']
        labels ={
            'idProducto': 'ID', 
            'nombreProducto': 'Nombre', 
            'descripcionProducto': 'Descripcion', 
            'precioProducto': 'Precio',
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese ID', 
                    'id': 'idProducto'
                }
            ), 
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre del Producto', 
                    'id': 'nombreProducto'
                }
            ), 
            'descripcionProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la Descripcion del Producto', 
                    'id': 'descripcionProducto'
                }
            ), 
            'precioProducto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Precio del Producto', 
                    'id': 'precioProducto'
                }
            )

        }


class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['correoCliente', 'nombreCliente', 'contraseñaCliente', 'nacionalidadCliente', 'sexoCliente', 'fechaCliente', 'telefonoCliente']
        labels ={
            'correoCliente': 'Correo Electronico', 
            'nombreCliente': 'Nombre Cliente', 
            'contraseñaCliente': 'Contraseña', 
            'nacionalidadCliente': 'Nacionalidad',
            'sexoCliente': 'Sexo',
            'fechaCliente': 'Fecha de Nacimiento',
            'telefonoCliente': 'Telefono Cliente',
        }
        widgets={
            'correoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correoCliente', 
                    'id': 'correoCliente'
                }
            ), 
            'nombreCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Nombre del Cliente', 
                    'id': 'nombreCliente'
                }
            ), 
            'contraseñaCliente': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la contraseña', 
                    'id': 'contraseñaCliente'
                }
            ), 
            'nacionalidadCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la nacionalidad', 
                    'id': 'nacionalidadCliente'
                }
            )
            , 
            'sexoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Sexo', 
                    'id': 'precioProducto'
                }
            ), 
            'fechaCliente': forms.DateInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese la fecha de nacimiento', 
                    'id': 'fechaCliente'
                }
            ), 
            'telefonoCliente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese el Teléfono del Cliente', 
                    'id': 'telefonoCliente'
                }
            )
            
            

        }