from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('producto/', producto, name="producto"),
    path('registro/', registro, name="registro"),
    path('tienda/', tienda, name="tienda"),
    path('cerrar_sesion/', cerrar_sesion, name="CERRAR_SESSION"),


    # Carrito
    path('carrito/', carrito, name="carrito"),
    
    # Metodos del Carrito
    path('agregar/<int:id_producto>/', agregar_al_carrito, name='AGREGAR_AL_CARRITO'),
    path('eliminar/<int:id_item>/', eliminar_del_carrito, name='ELIMINAR_DEL_CARRITO'),
    path('vaciar/', vaciar_carrito, name='VACIAR_CARRITO'),

    path('aumentar/<int:id_item>/', aumentar_cantidad, name='AUMENTAR_CANTIDAD'),
    path('disminuir/<int:id_item>/', disminuir_cantidad, name='DISMINUIR_CANTIDAD'),

    #miindicador

    path('indicadores/', indicadores_view, name='indicadores'),




]
