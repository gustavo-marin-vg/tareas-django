from django.db import models
from django.conf import settings

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, default=1)

    def __str__(self):
        return f"{self.id} | {self.titulo} | Completado: {self.completado}"
