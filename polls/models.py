# Create your models here.
from django.db import models


class Direccion(models.Model):
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=30)
    ciuadad = models.CharField(max_length=30)

    def __str__(self):
        return self.calle


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripccion = models.TextField()

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.BigIntegerField()
    direccion = models.IntegerField()
    web = models.URLField()

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    fecha = models.DateField()
    descuento = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha


class Telefono(models.Model):
    telefono = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefono


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Detalle(models.Model):
    cantidad = models.IntegerField()
