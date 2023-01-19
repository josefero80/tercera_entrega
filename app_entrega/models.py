from django.db import models

# Create your models here.

class Alimento(models.Model):
    categoria_al = models.CharField(max_length=256)
    nombre_al = models.CharField(max_length=256)
    precio_al = models.FloatField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombre_al} {self.categoria_al} {self.precio_al}'

class Accesorio(models.Model):
    nombre_ac = models.CharField(max_length=256)
    categoria_ac = models.CharField(max_length=256)
    precio_ac = models.FloatField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombre_ac} {self.categoria_ac} {self.precio_ac}'

class Juguete(models.Model):
    nombre_ju = models.CharField(max_length=256)
    categoria_ju = models.CharField(max_length=256)
    precio_ju = models.FloatField(max_length=4)

    def __str__(self) -> str:
        return f'{self.nombre_ju} {self.categoria_ju} {self.precio_ju}'
