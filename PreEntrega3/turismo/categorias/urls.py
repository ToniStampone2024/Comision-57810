from django.urls import path, include
from categorias.views import *

urlpatterns = [
    path('', home, name="home"),
    path('vuelos/', vuelos, name="vuelos"),
    path('hoteles/', hoteles, name="hoteles"),
    path('traslados/', traslados, name="traslados"),
    path('alquilerautos/', alquilerautos, name="alquilerautos"),

    #____ Formularios
    path('vueloForm/', vueloForm, name="vueloForm"),
    path('hotelForm/', hotelForm, name="hotelForm"),
    path('trasladoForm/', trasladoForm, name="trasladoForm"),
    path('alquilerautoForm/', alquilerautoForm, name="alquilerautoForm"),
    
    #--path('buscarCursos/', buscarCursos, name="buscarCursos"),
    #--path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),
    #--path('acerca/', acerca, name="acerca"),
]