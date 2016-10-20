from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.blog, name="main"),
	url(r'^$', views.blog, name="main"),
	url(r'^subscribe/$', views.subscribe, name="subscribe"),
]