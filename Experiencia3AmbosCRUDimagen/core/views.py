from urllib import request
from django.shortcuts import render, redirect
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm
# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')

def Registro(request):
    return render(request, 'Registro.html')

def Galeria(request):
    return render(request, 'Galeria.html')

def Somos(request):
    return render(request, 'Somos.html')

def Contacto(request):
    return render(request, 'Contacto.html')

def calculadora(request):
    return render(request, 'calculadora.html')
    
def apiMonedas(request):
    return render(request, 'apiMonedas.html')

def MostrarCliente(request):
    clientes = Cliente.objects.all()

    datos= {
        'clientes' : clientes
    }
    return render(request, 'MostrarCliente.html', datos)

def MostrarProducto(request):
    productos = Producto.objects.all()

    datos= {
        'productos' : productos
    }
    return render(request, 'MostrarProducto.html', datos)


def CrearCliente(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid:
            cliente_form.save()
            return redirect ('MostrarCliente')
    else:
        cliente_form =ClienteForm()
    return render(request, 'CrearCliente.html', {'cliente_form': cliente_form})


def CrearProducto(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid:
            producto_form.save()
            return redirect ('MostrarProducto')
    else:
        producto_form =ProductoForm()
    return render(request, 'CrearProducto.html', {'producto_form': producto_form})


def ModificarCliente(request,id):
    cliente = Cliente.objects.get(correoCliente=id)
    datos={
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario=ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid:
            formulario.save()
            return redirect('MostrarCliente')
    
    return render(request, 'ModificarCliente.html', datos)

def ModificarProducto(request,id):
    producto = Producto.objects.get(idProducto=id)
    datos={
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            return redirect('MostrarProducto')
    
    return render(request, 'ModificarProducto.html', datos)

def EliminarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('MostrarProducto')

def EliminarCliente(request, id):
    cliente = Cliente.objects.get(correoCliente=id)
    cliente.delete()
    return redirect('MostrarCliente')

 

