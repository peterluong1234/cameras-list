from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Camera
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cameras_index(request):
    cameras = Camera.objects.all()
    return render(request, 'cameras/index.html', { 'cameras': cameras })

def cameras_detail(request, camera_id):
    camera = Camera.objects.get(id=camera_id)
    return render(request, 'cameras/detail.html', { 'camera': camera })

class CameraCreate(CreateView):
    model = Camera
    fields = '__all__'
    success_url = '/cameras/'

class CameraUpdate(UpdateView):
    model = Camera
    fields = ['brand', 'resolution', 'description']

class CameraDelete(DeleteView):
    model = Camera
    success_url = '/cameras/'