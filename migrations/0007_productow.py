# Generated by Django 3.2.6 on 2022-06-19 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0006_remove_contacto_avisos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('descripcion', models.TextField(max_length=50, verbose_name='Descripcion producto')),
                ('precio', models.IntegerField(verbose_name='Precio producto')),
                ('nuevo', models.BooleanField(verbose_name='Nuevo')),
                ('fecha_fabricacion', models.DateField(verbose_name='Fecha fabricacion')),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tienda.marca')),
            ],
        ),
    ]