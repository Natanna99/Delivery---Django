# Generated by Django 3.0.4 on 2020-06-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_delivery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='pratos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='pratos',
            field=models.ManyToManyField(to='app_delivery.Cesta'),
        ),
    ]
