# Generated by Django 5.1.1 on 2025-03-06 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paquete_interesados', '0002_remove_historicalcol_interesado_ext_pid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalCR_Interesado',
        ),
    ]
