from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^registration$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]