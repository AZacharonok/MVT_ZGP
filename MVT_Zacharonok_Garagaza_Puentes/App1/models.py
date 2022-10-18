from django.db import models


class familiar(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=200)
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.dni}, {self.id}"