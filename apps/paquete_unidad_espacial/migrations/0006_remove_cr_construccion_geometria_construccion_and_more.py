# Generated by Django 5.1.1 on 2025-05-17 20:04

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paquete_unidad_espacial', '0005_remove_cr_terreno_geometria_terreno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cr_construccion',
            name='geometria_construccion',
        ),
        migrations.RemoveField(
            model_name='cr_unidadconstruccion',
            name='geometria_unidad_construccion',
        ),
        migrations.RemoveField(
            model_name='historicalcr_construccion',
            name='geometria_construccion',
        ),
        migrations.RemoveField(
            model_name='historicalcr_unidadconstruccion',
            name='geometria_unidad_construccion',
        ),
        migrations.AddField(
            model_name='cr_construccion',
            name='construccion_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Construcción'),
        ),
        migrations.AddField(
            model_name='cr_unidadconstruccion',
            name='unidad_construccion_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Unidad Construcción'),
        ),
        migrations.AddField(
            model_name='historicalcr_construccion',
            name='construccion_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Construcción'),
        ),
        migrations.AddField(
            model_name='historicalcr_unidadconstruccion',
            name='unidad_construccion_geometria',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, help_text='Corresponde a la figura geometrica vectorial poligonal, generada a partir de los linderos del predio.', null=True, srid=4326, verbose_name='Geometría Unidad Construcción'),
        ),
    ]
