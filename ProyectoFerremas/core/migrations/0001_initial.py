# Generated by Django 5.0.4 on 2024-05-22 00:25

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(default=django.utils.timezone.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='productos/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='CarritoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoempleado')),
            ],
        ),
    ]
