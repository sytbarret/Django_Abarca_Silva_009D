# Generated by Django 4.0.5 on 2022-06-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_descripcionproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombreProducto',
            field=models.CharField(max_length=100, verbose_name='Nombre Producto'),
        ),
    ]