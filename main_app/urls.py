from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cameras/', views.cameras_index, name='index'),
    path('cameras/<int:camera_id>', views.cameras_detail, name='detail'),
    path('cameras/create/', views.CameraCreate.as_view(), name='cameras_create'),
    path('cameras/<int:pk>/update', views.CameraUpdate.as_view(), name='cameras_update'),
    path('cameras/<int:pk>/delete/', views.CameraDelete.as_view(), name='cameras_delete'),
    path('lenses/', views.LensList.as_view(), name='lenses_index'),
    path('lenses/<int:pk>/', views.LensDetail.as_view(), name='lenses_detail'),
    path('lenses/create/', views.LensCreate.as_view(), name='lenses_create'),
    path('lenses/<int:pk>/update/', views.LensUpdate.as_view(), name='lenses_update'),
    path('lenses/<int:pk>/delete/', views.LensDelete.as_view(), name='lenses_delete'),
    path('cameras/<int:camera_id>/assoc_lens/<int:lens_id>/', views.assoc_lens, name='assoc_lens'),
]