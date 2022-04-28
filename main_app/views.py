from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Camera, Lens
from .forms import RecallForm

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
    lens_camera_doesnt_have = Lens.objects.exclude(id__in = camera.lens.all().values_list('id'))

    recall_form = RecallForm()

    return render(request, 'cameras/detail.html', { 
        'camera': camera, 
        'recall_form': recall_form,
        'lens': lens_camera_doesnt_have
    })

class CameraCreate(CreateView):
    model = Camera
    fields = '__all__'
    success_url = '/cameras/'

class CameraUpdate(UpdateView):
    model = Camera
    fields = '__all__'

class CameraDelete(DeleteView):
    model = Camera
    success_url = '/cameras/'

class LensList(ListView):
  model = Lens

class LensDetail(DetailView):
  model = Lens

class LensCreate(CreateView):
  model = Lens
  fields = '__all__'

class LensUpdate(UpdateView):
  model = Lens
  fields = ['name', 'lens_mount', 'focal_length', 'aperture']

class LensDelete(DeleteView):
  model = Lens
  success_url = '/lenses/'

def assoc_lens(request, camera_id, lens_id):
  # Note that you can pass a toy's id instead of the whole object
  Camera.objects.get(id=camera_id).lens.add(lens_id)
  return redirect('detail', camera_id=camera_id)