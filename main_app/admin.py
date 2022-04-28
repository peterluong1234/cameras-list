from django.contrib import admin
# import your models here
from .models import Camera, Recall

# Register your models here
admin.site.register(Camera)
admin.site.register(Recall)