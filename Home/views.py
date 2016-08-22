from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'Home/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'Home/detail.html', {'album': album})