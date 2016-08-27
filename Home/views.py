from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'Home/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'Home/detail.html'