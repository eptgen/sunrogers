
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.main, name="main"),
	url(r'^on/$', views.on, name="on"),
	url(r'^off/$', views.off, name="off"),
	url(r'^toggle/$', views.toggle, name="toggle"),
	url(r'^get/$', views.get, name="get"),
]