from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    stock = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
