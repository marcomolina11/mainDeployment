from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.allNinjas),
    url(r'^ninjas/(?P<color>[a-z]+)$', views.showNinjas)
]