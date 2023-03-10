# Generated by Django 4.1.4 on 2023-01-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ac', models.CharField(max_length=256)),
                ('categoria_ac', models.CharField(max_length=256)),
                ('precio_ac', models.FloatField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_al', models.CharField(max_length=256)),
                ('nombre_al', models.CharField(max_length=256)),
                ('precio_al', models.FloatField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='juguete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ju', models.CharField(max_length=256)),
                ('categoria_ju', models.CharField(max_length=256)),
                ('precio_ju', models.FloatField(max_length=4)),
            ],
        ),
    ]
