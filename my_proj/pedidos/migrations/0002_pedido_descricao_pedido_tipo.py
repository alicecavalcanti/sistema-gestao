# Generated by Django 4.1.13 on 2024-10-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='descricao',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
