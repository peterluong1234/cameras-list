from django.db import models
from django.urls import reverse

# Create your models here.

DEGREES = (
    ('MN', 'Minor'),
    ('MJ', 'Major')
)

class Lens(models.Model):
    name = models.CharField(max_length=20)
    lens_mount = models.CharField(max_length=50)
    focal_length = models.CharField(max_length=50)
    aperture = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lenses_detail', kwargs={'pk': self.id})

    
class Camera(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    lens_mount = models.CharField(max_length=50)
    sensor = models.CharField(max_length=50)
    resolution = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=250)
    lens = models.ManyToManyField(Lens)
    
    def __str__(self):
        return f"{self.brand} {self.name}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'camera_id': self.id})


class Recall(models.Model):
    date = models.DateField('Recall Date')
    degree = models.CharField(
        max_length=2,
        choices=DEGREES,
        default=DEGREES[0][0]
    )

    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_degree_display()} recall on {self.date}"

    class Meta:
        ordering = ['-date']
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for camera_id: {self.camera_id} @{self.url}"