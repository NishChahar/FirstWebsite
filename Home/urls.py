from django.conf.urls import url
from . import views

urlpatterns = [
    #/Home/
    url(r'^$', views.index, name='index'),

    #/Home/123(id)
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
