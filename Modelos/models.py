from django.db import models

# Create your models here.
class Fruta(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)