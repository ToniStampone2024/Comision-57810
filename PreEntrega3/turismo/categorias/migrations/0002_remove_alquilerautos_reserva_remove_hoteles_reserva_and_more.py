# Generated by Django 4.2.13 on 2024-07-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alquilerautos',
            name='reserva',
        ),
        migrations.RemoveField(
            model_name='hoteles',
            name='reserva',
        ),
        migrations.RemoveField(
            model_name='traslados',
            name='reserva',
        ),
        migrations.RemoveField(
            model_name='vuelos',
            name='reserva',
        ),
    ]
