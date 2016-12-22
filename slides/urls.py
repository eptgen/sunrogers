
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, "home"),
	url(r'^change/show/$', views.change_show, "changeshow"),
	url(r'^change/slide/$', views.change_slide, "changeslide"),
	url(r'^data/$', views.data, "data"),
]