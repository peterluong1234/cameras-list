from django.db import models

# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    sensor = models.CharField(max_length=50)
    resolution = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return f"{self.brand} {self.name}"