from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.

def home(request):
    return render(request, "categorias/index.html")

def vuelos(request):
    contexto = {"vuelos": Vuelos.objects.all()}
    return render(request, "categorias/vuelos.html", contexto)

def hoteles(request):
    contexto = {"hoteles": Hoteles.objects.all()}
    return render(request, "categorias/hoteles.html")

def traslados(request):
    contexto = {"traslados": Traslados.objects.all()}
    return render(request, "categorias/traslados.html")

def alquilerautos(request):
    contexto = {"alquilerautos": AlquilerAutos.objects.all()}
    return render(request, "categorias/alquilerautos.html")

#___ Formularios
def vueloForm(request):
    if request.method == "POST":
        miForm = VueloForm(request.POST)
        if miForm.is_valid():
            v_aerolinea     = miForm.cleaned_data.get("aerolinea")
            v_mail          = miForm.cleaned_data.get("mail")
            v_numero        = miForm.cleaned_data.get("numero")
            v_origen        = miForm.cleaned_data.get("origen")
            v_destino       = miForm.cleaned_data.get("destino")
            v_fecha         = miForm.cleaned_data.get("fecha")
            v_hora          = miForm.cleaned_data.get("hora")
            v_precio        = miForm.cleaned_data.get("precio")
            v_fecha_reserva = miForm.cleaned_data.get("fecha_reserva")
            v_fecha_compra  = miForm.cleaned_data.get("fecha_compra")
            v_usuario       = miForm.cleaned_data.get("usuario")
            
            vuelo = Vuelos(aerolinea=v_aerolinea, mail=v_mail, numero=v_numero, origen=v_origen,
                           destino=v_destino, fecha=v_fecha, hora=v_hora, precio=v_precio,
                           fecha_reserva=v_fecha_reserva, fecha_compra=v_fecha_compra,
                           usuario=v_usuario)
            
            vuelo.save()
            contexto = {"vuelos": Vuelos.objects.all() }
            return render(request, "categorias/vuelos.html", contexto)
    else:
        miForm = VueloForm()
    
    return render(request, "categorias/vueloForm.html", {"form": miForm})


def hotelForm(request):
    if request.method == "POST":
        miForm = HotelForm(request.POST)
        if miForm.is_valid():
            h_nombre         = miForm.cleaned_data.get("nombre")
            h_mail           = miForm.cleaned_data.get("mail")
            h_ciudad         = miForm.cleaned_data.get("ciudad")
            h_pais           = miForm.cleaned_data.get("pais")
            h_direccion      = miForm.cleaned_data.get("direccion")
            h_estrellas      = miForm.cleaned_data.get("estrellas")
            h_fecha_desde    = miForm.cleaned_data.get("fecha_desde")
            h_fecha_hasta    = miForm.cleaned_data.get("fecha_hasta")
            h_precio         = miForm.cleaned_data.get("precio")
            h_fecha_reserva  = miForm.cleaned_data.get("fecha_reserva")
            h_fecha_compra   = miForm.cleaned_data.get("fecha_compra")
            h_usuario        = miForm.cleaned_data.get("usuario")
            
            hotel = Hoteles(nombre        = h_nombre,
                            mail          = h_mail, 
                            ciudad        = h_ciudad, 
                            pais          = h_pais,
                            direccion     = h_direccion, 
                            estrellas     = h_estrellas, 
                            fecha_desde   = h_fecha_desde, 
                            fecha_hasta   = h_fecha_hasta,
                            precio        = h_precio,
                            fecha_reserva = h_fecha_reserva,
                            fecha_compra  = h_fecha_compra,
                            usuario       = h_usuario)
            
            hotel.save()
            contexto = {"hoteles": Hoteles.objects.all() }
            return render(request, "categorias/hoteles.html", contexto)
    else:
        miForm = HotelForm()
    
    return render(request, "categorias/hotelForm.html", {"form": miForm})


def trasladoForm(request):
    if request.method == "POST":
        miForm = TrasladoForm(request.POST)
        if miForm.is_valid():
            t_nombre         = miForm.cleaned_data.get("nombre")
            t_mail           = miForm.cleaned_data.get("mail")
            t_ciudad         = miForm.cleaned_data.get("ciudad")
            t_pais           = miForm.cleaned_data.get("pais")
            t_origen         = miForm.cleaned_data.get("origen")
            t_destino        = miForm.cleaned_data.get("destino")
            t_fecha          = miForm.cleaned_data.get("fecha")
            t_hora           = miForm.cleaned_data.get("hora")
            t_precio         = miForm.cleaned_data.get("precio")
            t_fecha_reserva  = miForm.cleaned_data.get("fecha_reserva")
            t_fecha_compra   = miForm.cleaned_data.get("fecha_compra")
            t_usuario        = miForm.cleaned_data.get("usuario")
            
            traslado = Traslados(nombre=t_nombre, mail=t_mail, ciudad=t_ciudad, pais=t_pais,
                           origen=t_origen, destino=t_destino, fecha=t_fecha, 
                           hora=t_hora, precio=t_precio,
                           fecha_reserva=t_fecha_reserva, fecha_compra=t_fecha_compra,
                           usuario=t_usuario)
            
            traslado.save()
            contexto = {"traslados": Traslados.objects.all() }
            return render(request, "categorias/traslados.html", contexto)
    else:
        miForm =TrasladoForm()
    
    return render(request, "categorias/trasladoForm.html", {"form": miForm})


def alquilerautoForm(request):
    if request.method == "POST":
        miForm = AlquilerautoForm(request.POST)
        if miForm.is_valid():
            a_nombre            = miForm.cleaned_data.get("nombre")
            a_mail              = miForm.cleaned_data.get("mail")
            a_clase             = miForm.cleaned_data.get("clase")
            a_anio_fabricacion  = miForm.cleaned_data.get("anio_fabricacion")
            a_ciudad            = miForm.cleaned_data.get("ciudad")
            a_pais              = miForm.cleaned_data.get("pais")
            a_direccion_agencia = miForm.cleaned_data.get("direccion_agencia")
            a_fecha_desde       = miForm.cleaned_data.get("fecha_desde")
            a_fecha_hasta       = miForm.cleaned_data.get("fecha_hasta")
            a_precio            = miForm.cleaned_data.get("precio")
            a_fecha_reserva     = miForm.cleaned_data.get("fecha_reserva")
            a_fecha_compra      = miForm.cleaned_data.get("fecha_compra")
            a_usuario           = miForm.cleaned_data.get("usuario")
            
            alquilerauto = AlquilerAutos(nombre=a_nombre, mail=a_mail, clase=a_clase, 
                           anio_fabricacion=a_anio_fabricacion,
                           ciudad=a_ciudad, pais=a_pais, direccion_agencia=a_direccion_agencia,
                           fecha_desde=a_fecha_desde, fecha_hasta=a_fecha_hasta, precio= a_precio,
                           fecha_reserva=a_fecha_reserva,
                           fecha_compra=a_fecha_compra, usuario=a_usuario)
                           
            
            alquilerauto.save()
            contexto = {"alquilerautos": AlquilerAutos.objects.all() }
            return render(request, "categorias/alquilerautos.html", contexto)
    else:
        miForm =TrasladoForm()
    
    return render(request, "categorias/alquilerautoForm.html", {"form": miForm})
