from django.db import models

# Create your models here.
class usuarios(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)