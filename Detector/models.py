from django.db import models

# Create your models here.
class Entrada(models.Model):
    HoraEntrada = models.DateTimeField(max_length=30)
    