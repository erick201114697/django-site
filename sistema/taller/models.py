from django.urls import reverse
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    nit = models.CharField(max_length=12)
    telefono = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=32)
    modelo = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.marca} - {self.modelo}'


class Servicio(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField()
    anotaciones = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.vehiculo} - {self.fecha}'

class Cine(models.Model):
    nombre = models.CharField(max_length=256)
    dirccion = models.CharField(max_length=256)
    telefono = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=256)
    numero = models.CharField(max_length=256)
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.nombre} {self.numero} - {self.cine}'


class Fila(models.Model):
    fila = models.CharField(max_length=256)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Fila {self.fila} - {self.sala}'

class Pelicula(models.Model):
    nombre = models.CharField(max_length=256)
    fechaestreno = models.DateField()
    preciotaquilla = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'{self.nombre} - Estreno: {self.fechaestreno} - Precio taquilla Q{self.preciotaquilla}' 