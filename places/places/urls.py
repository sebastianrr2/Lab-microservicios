from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.PlacesList, name='placesList'),
    url(r'^placescreate/$', csrf_exempt(views.PlacesCreate), name='placesCreate'),
]