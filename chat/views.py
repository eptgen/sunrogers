
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout

from .models import Chat, Post

# Create your views here.

def home(request): # also serves as authentication
	if request.method == "post":
		pass
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("chats:chats"))
		return HttpResponseRedirect(reverse("chats:login"))
	
def login(request): # post-logout
	if request.method == "post":
		pass
	else:
		if request.session.get("jlo"):
			request.session.set("jlo", False)
			return render(request, "chats.login.html", {"success": "You have logged out."})
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("chats:chats"))
		return render(request, "chats/login.html", {})
	
def logout(request):
	if request.user.is_authenticated:
		logout(request)
		request.session.set("jlo", True)
		return HttpResponseRedirect(reverse("chats:login"))
	else:
		return HttpResponseRedirect(reverse("chats:login"))

def new_account(request):
	if request.method == "post":
		pass
	else:
		return render(request, "chats/newaccount.html", {})
	
def chats(request):
	chats_for_user = 
	
def viewchat(request, chat_id):
	pass
	
def new_chat(request):
	pass
	
def new_post(request):
	pass


































