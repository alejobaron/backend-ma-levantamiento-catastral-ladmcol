# Generated by Django 5.1.1 on 2025-05-17 11:55

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paquete_unidad_espacial', '0004_historicalcol_unidadespacial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cr_terreno',
            name='geometria_terreno',
        ),
        migrations.RemoveField(
            model_name='historicalcr_terreno',
            name='geometria_terreno',
        ),
        migrations.AddField(
            model_name='cr_terreno',
            name='terreno_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Terreno'),
        ),
        migrations.AddField(
            model_name='historicalcr_terreno',
            name='terreno_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Terreno'),
        ),
    ]
