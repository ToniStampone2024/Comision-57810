from django.db import models

# Create your models here.
# Modelo de Negocio de la Aplicacion

class Vuelos(models.Model): 
    aerolinea      = models.CharField(max_length=50)
    mail           = models.EmailField()
    numero         = models.CharField(max_length=6)
    origen         = models.CharField(max_length=50)
    destino        = models.CharField(max_length=50)
    fecha          = models.DateField()
    hora           = models.CharField(max_length=4)
    precio         = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_reserva  = models.DateField()
    fecha_compra   = models.DateField()
    usuario        = models.CharField(max_length=50)


class Hoteles(models.Model):
    nombre         = models.CharField(max_length=50)
    mail           = models.EmailField()
    ciudad         = models.CharField(max_length=50)
    pais           = models.CharField(max_length=50)
    direccion      = models.CharField(max_length=60)
    estrellas      = models.IntegerField()
    fecha_desde    = models.DateField()
    fecha_hasta    = models.DateField()
    precio         = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_reserva  = models.DateField()
    fecha_compra   = models.DateField()
    usuario        = models.CharField(max_length=50)


class Traslados(models.Model):
    nombre         = models.CharField(max_length=50)
    mail           = models.EmailField()
    ciudad         = models.CharField(max_length=50)
    pais           = models.CharField(max_length=50)
    origen         = models.CharField(max_length=50)
    destino        = models.CharField(max_length=50)
    fecha          = models.DateField()
    hora           = models.CharField(max_length=4)
    precio         = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_reserva  = models.DateField()
    fecha_compra   = models.DateField()
    usuario        = models.CharField(max_length=50)
    

class AlquilerAutos(models.Model):
    nombre            = models.CharField(max_length=50)
    mail              = models.EmailField()
    clase             = models.CharField(max_length=50)
    anio_fabricacion  = models.PositiveIntegerField()
    ciudad            = models.CharField(max_length=50)
    pais              = models.CharField(max_length=50)
    direccion_agencia = models.CharField(max_length=50)
    fecha_desde       = models.DateField()
    fecha_hasta       = models.DateField()
    precio            = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_reserva     = models.DateField()
    fecha_compra      = models.DateField()
    usuario           = models.CharField(max_length=50)
    

