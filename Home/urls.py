from django.conf.urls import url
from . import views

app_name = 'Home'

urlpatterns = [
    #/Home/
    url(r'^$', views.index, name='index'),

    #/Home/123(id)
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    #/Home/Favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]
