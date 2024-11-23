from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Extintor(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.TextField()
    cantidad = models.IntegerField()


    def __str__(self):
        return self.nombre