
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.pretty, name="pretty"),
	url(r'^get/$', views.gett, name="get"),
	url(r'^change/$', views.change, name="change"),
]