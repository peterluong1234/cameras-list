from django.db import models
from django.urls import reverse

# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    lens_mount = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)
    resolution = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    # Lens = models.ManyToManyField(Lens)
    
    def __str__(self):
        return f"{self.brand} {self.name}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'camera_id': self.id})

class Lens(models.Model):
    name = models.CharField(max_length=20)
    lens_mount = models.CharField(max_length=50)
    focal_length = models.CharField(max_length=50)
    aperture = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lenses_detail', kwargs={'pk': self.id})

    
