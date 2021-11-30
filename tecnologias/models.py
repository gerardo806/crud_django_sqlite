from django.db import models

class comentarios(models.Model):
    usuario = models.CharField(max_length=30)
    comentario = models.CharField(max_length=255)


