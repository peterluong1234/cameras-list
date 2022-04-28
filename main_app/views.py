from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Camera, Lens, Recall, Photo
from .forms import RecallForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'cameracollector'

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

def add_recall(request, camera_id):
    form = RecallForm(request.POST)
     # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
        new_recall = form.save(commit=False)
        new_recall.camera_id = camera_id
        new_recall.save()
    return redirect('detail', camera_id=camera_id)

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

def add_photo(request, camera_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            Photo.objects.create(url=url, camera_id=camera_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', camera_id=camera_id)