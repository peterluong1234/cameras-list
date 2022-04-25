from django.shortcuts import render
from .models import Camera
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def cameras_index(request):
    cameras = Camera.objects.all()
    return render(request, 'cameras/index.html', { 'cameras': cameras })

def cameras_detail(request, camera_id):
    camera = Camera.objects.get(id=camera_id)
    return render(request, 'cameras/detail.html', { 'camera': camera })