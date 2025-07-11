# Generated by Django 5.1.1 on 2025-05-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estructuras', '0005_alter_col_areavalor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='col_areavalor',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='col_volumenvalor',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='extarchivo',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='extdireccion',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='extinteresado',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='gm_multisurface3d',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalcol_areavalor',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalcol_volumenvalor',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalextarchivo',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalextdireccion',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalextinteresado',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicalgm_multisurface3d',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicallc_estructuranovedadnumeropredial',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='historicallc_novedadfmi',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='lc_estructuranovedadnumeropredial',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
        migrations.AlterField(
            model_name='lc_novedadfmi',
            name='deleted_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Elimnación'),
        ),
    ]
