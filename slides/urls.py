
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, "home"),
	url(r'^nextslide/$', views.next_slide, "nextslide"),
	url(r'^prevslide/$', views.prev_slide, "prevslide"),
	url(r'^change/show/$', views.change_show, "changeshow"),
	url(r'^change/slide/$', views.change_slide, "changeslide"),
	url(r'^data/$', views.data, "data"),
]