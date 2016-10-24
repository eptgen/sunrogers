
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^login/$', views.login, name="login"),
	url(r'^logout/$', views.logout, name="logout"),
	url(r'^create/account/$', views.new_account, name="newaccount"),
	url(r'^chats/', views.chats, name="chats"),
	url(r'^chats/(?P<chat_id>)/', views.viewchat, name="viewchat"),
	url(r'^create/chat/$', views.new_chat, name="newchat"),
	url(r'^create/post/$', views.new_post, name="newpost"),
]