# Generated by Django 4.0.3 on 2022-03-13 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myFindings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estancia',
            old_name='croquis_plata',
            new_name='croquis_planta',
        ),
    ]
