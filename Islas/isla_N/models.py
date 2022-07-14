from django.db import models

# Create your models here.

class PlanesServiciosEspeciales(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

#Columna
class PlanesMorarbe(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class PlanesKonecta(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class PlanesWTA(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class NumerosAxxaAssistance(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
