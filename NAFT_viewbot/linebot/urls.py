from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^callback', views.callback),
    url(r'^$', views.index, name="index")
]
