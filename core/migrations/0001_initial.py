# Generated by Django 4.0.5 on 2022-06-08 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=20, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='N° registro')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo Noticia')),
                ('fecha', models.CharField(max_length=10, verbose_name='Fecha')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicacion')),
                ('descripcion', models.CharField(max_length=2000, verbose_name='Cuerpo de la noticia')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
