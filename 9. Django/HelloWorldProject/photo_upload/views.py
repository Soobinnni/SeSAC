from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Photo

# Create your views here.
def photo_upload(request:HttpRequest)-> HttpResponse:
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        photo = Photo.objects.create(title = title, image = image)
        photo.save()
        return redirect('photo_list')
    return render(request, 'photo_upload/photo_upload.html')


def photo_list(request:HttpRequest)-> HttpResponse:
    photos = Photo.objects.all()

    return render(request, 'photo_upload/photo_list.html', {'photos' : photos})