# Generated by Django 4.1.13 on 2024-10-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField(default=0)),
                ('validade', models.DateField()),
                ('fornecedor', models.CharField(max_length=200)),
            ],
        ),
    ]
