
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.view, name="view"),
	url(r'^((?P<num>[0-9]+))?$', views.view, name="view"),
	url(r'^random/', views.random_comic, name="random"),
]