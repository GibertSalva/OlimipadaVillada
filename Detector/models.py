from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Localizacion(models.Model):
    provincia = models.CharField(max_length=20)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()

    def __str__(self):
        return "{}".format(self.provincia)

class Sensor(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.nombre1)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=30)
    capacidadMaxima = models.IntegerField()
    localizacion = models.ForeignKey('Localizacion', on_delete=models.CASCADE,null=False)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    sensor_ingreso = models.ForeignKey('Sensor', on_delete=models.CASCADE, null=False, related_name='%(class)s_requests_created')
    sensor_egreso = models.ForeignKey('Sensor', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return "{}".format(self.nombre)


class Entrada(models.Model):
    hora_entrada = models.DateTimeField(auto_now_add=True)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE,null=False)

    def __str__(self):
        return "{}".format(self.hora_entrada)


class Salida(models.Model):
    hora_salida = models.DateTimeField(auto_now_add=True)
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE,null=False)


    