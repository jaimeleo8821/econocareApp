# Generated by Django 5.0.1 on 2024-02-03 14:30

import autoslug.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=100, verbose_name='Origen')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=150, populate_from='origin', unique=True)),
            ],
            options={
                'verbose_name': 'Origen del Movimiento',
                'verbose_name_plural': 'Orígenes del Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Pay_Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payMethod', models.CharField(max_length=100, verbose_name='Método de Pago')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=150, populate_from='payMethod', unique=True)),
            ],
            options={
                'verbose_name': 'Método de Pago',
                'verbose_name_plural': 'Métodos de Pago',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Tipo')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=150, populate_from='type', unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Movimiento',
                'verbose_name_plural': 'Tipos de Movimientos',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='Categoría')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=150, populate_from='category', unique=True)),
                ('idType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movements.type', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Categoría de Movimiento',
                'verbose_name_plural': 'Categoría de Movimientos',
                'unique_together': {('id', 'idType')},
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('observations', models.CharField(max_length=100, verbose_name='Observaciones')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, max_length=150, populate_from='id', unique=True)),
                ('idCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movements.category', verbose_name='Categoría')),
                ('idUser', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('idOrigin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movements.origin', verbose_name='Origen')),
                ('idPayMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movements.pay_method', verbose_name='Método de Pago')),
                ('idType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movements.type', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
                'unique_together': {('id', 'idOrigin', 'idType', 'idCategory', 'idPayMethod', 'idUser')},
            },
        ),
    ]
