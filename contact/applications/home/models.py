from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    
    def __str__(self):
        return str(self.id) + '-'+ self.nombre + '-' + self.apellidos

