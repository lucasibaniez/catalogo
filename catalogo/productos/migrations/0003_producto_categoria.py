# Generated by Django 4.0.8 on 2022-12-14 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
        ('productos', '0002_producto_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria'),
        ),
    ]
