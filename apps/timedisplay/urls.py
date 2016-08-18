from django.conf.urls import url
from . import views
 #url(r'^users$', views.show)
urlpatterns = [
    url(r'^$', views.index),
]