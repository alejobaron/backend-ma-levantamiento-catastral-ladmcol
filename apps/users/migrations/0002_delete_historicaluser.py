# Generated by Django 5.1.1 on 2025-03-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalUser',
        ),
    ]
