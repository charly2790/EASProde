# Generated by Django 4.0.4 on 2022-11-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prode', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipos',
            options={'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AddField(
            model_name='equipos',
            name='img_bandera',
            field=models.ImageField(blank=True, default='imagenes_banderas/bandera-img-default.png', null=True, upload_to='imagenes_banderas'),
        ),
    ]
