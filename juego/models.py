from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length = 20)
    clave = models.CharField(max_length = 20)
    grado = models.IntegerField(default = 1)
    activo = models.BooleanField(default = True)

    def __str__(self):
        return self.nombre

    def esGrado(self):
        return self.grado

class Record(models.Model):
    JUEGOS = (
        ('1', 'JUEGO 1'),
        ('2', 'JUEGO 2'),
    )
    idUsuario = models.IntegerField(default = 0, primary_key = True)
    idJuego = models.CharField(max_length = 1, choices = JUEGOS)
    puntuacion = models.IntegerField(default = 0)
    fecha = models.DateTimeField('Fecha Jugado')

    def __str__(self):
        return self.idUsuario
