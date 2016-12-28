
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^nextslide/$', views.next_slide, name="nextslide"),
	url(r'^prevslide/$', views.prev_slide, name="prevslide"),
	url(r'^change/show/$', views.change_show, name="changeshow"),
	url(r'^change/slide/$', views.change_slide, name="changeslide"),
	url(r'^data/$', views.data, name="data"),
]