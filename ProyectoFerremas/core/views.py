from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, CarritoItem
import locale
import requests
from django.shortcuts import render

from django.contrib.auth import logout,authenticate,login as login_aut

# Create your views here.
def index (request):
    
    return render(request,'core/index.html')

def login (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_active:
            login_aut(request, user)
            return redirect(to='index')
    return render(request,'core/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect(to="index")

def producto (request):
    return render(request,'core/producto.html')

def registro (request):
    return render(request,'core/registro.html')

def tienda (request):
    productos = Producto.objects.all()
    ctx = {
        "productos" : productos
    }
    return render(request,'core/tienda.html', ctx)

# Carrito
def carrito(request):

    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

    carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
    items_carrito = carrito.carritoitem_set.all()
    sub_total_items = sum(item.cantidad * item.producto.precio for item in items_carrito)
    total = sum(item.precio_total() for item in items_carrito)
    total_formateado = locale.format_string("%d", total, grouping=True)

    for item in items_carrito:
        item.total_item = item.cantidad * item.producto.precio

    ctx = {
        'items_carrito': items_carrito,
        'total': total,
        'total_formato': total_formateado,
        'sub_total':sub_total_items
        }
    return render(request, 'core/carrito.html', ctx)

# METODOS DEL CARRITO
#@login_required(login_url='/login/')
def agregar_al_carrito(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
    item_existente = carrito.carritoitem_set.filter(producto=producto).first()
    
    if item_existente:
        # Si el producto ya está en el carrito, aumenta la cantidad
        item_existente.cantidad += 1
        item_existente.save()
    else:
        # Si el producto no está en el carrito, crea un nuevo ítem
        CarritoItem.objects.create(carrito=carrito, producto=producto, precio=producto.precio)
        
    return redirect('tienda')

#@login_required(login_url='/login/')
def eliminar_del_carrito(request, id_item):
    item = CarritoItem.objects.get(pk=id_item)
    item.delete()
    return redirect('carrito')

#@login_required(login_url='/login/')
def vaciar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.carritoitem_set.all().delete()
    return redirect('carrito')

# MAS METODOS
#@login_required(login_url='/login/')
def aumentar_cantidad(request, id_item):
    item = get_object_or_404(CarritoItem, pk=id_item)
    item.cantidad += 1
    item.save()
    return redirect('carrito')

#@login_required(login_url='/login/')
def disminuir_cantidad(request, id_item):
    item = get_object_or_404(CarritoItem, pk=id_item)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
    return redirect('carrito')

 
#miindicador
def indicadores_view(request):
    url = 'https://mindicador.cl/api'
    try:
        response = requests.get(url)
        data = response.json()
        indicadores = {
            'uf': data.get('uf', {}).get('valor'),
            'dolar': data.get('dolar', {}).get('valor'),
            'euro': data.get('euro', {}).get('valor'),
            'ipc': data.get('ipc', {}).get('valor'),
        }
    except Exception as e:
        indicadores = {}
        print(f"Error al obtener los datos de la API: {e}")

    return render(request, 'core/indicadores.html', {'indicadores': indicadores})

