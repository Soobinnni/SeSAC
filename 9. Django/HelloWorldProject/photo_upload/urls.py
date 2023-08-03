from django.urls import path
from . import views as view

urlpatterns = [
    path('upload/', view.photo_upload, name='photo_upload'),
    path('list/', view.photo_list, name='photo_list'),
]