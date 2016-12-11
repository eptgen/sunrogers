
from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout

from .models import Chat, Post, ChatPerm
from .forms import ChatForm, PostForm

# Create your views here.

def home(request): # also serves as authentication
	if request.method == "post":
		pass
	else:
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse("chats:chats"))
		return HttpResponseRedirect(reverse("chats:login"))
	
def login(request): # post-logout, and EVERYTHING redirects here if you aren't logged in
	if request.method == "post":
		pass
	else:
		if request.session.get("jlo"):
			request.session.set("jlo", False)
			return render(request, "chats/login.html", {"success": "You have logged out."})
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
	if request.user.is_authenticated:
		chats_for_user = ChatPerm.objects.filter(user=request.user).chat_set.order_by("create_date")
		return render(request, "chats/allchats.html", {"chats": chats_for_user, "user": request.user})
	else:
		return HttpResponseRedirect(reverse("chats:login"))
	
def viewchat(request, chat_id):
	if request.user.is_authenticated:
		chat = Chat.objects.filter(pk=chat_id)
		posts = Post.objects.filter(chat=chat)
		if ChatPerm.objects.filter(user=request.user).filter(chat=chat):
			form = PostForm()
			return render(request, "chats/chat.html", {"posts": posts, "user": request.user, "form": form})
		return HttpResponse("Hi sorry you bad bye")
	else:
		return HttpResponseRedirect(reverse("chats:login"))
	
def new_chat(request):
	if request.user.is_authenticated:
		if request.method == "post":
			form = ChatForm(request.POST)
			if form.is_valid():
				chat = Chat(owner = request.user, title = form.cleaned_data["title"], body = form.cleaned_data["body"], create_date = date.today())
				chat.save()
				chatperm = ChatPerm(chat = chat, user = request.user)
				return HttpResponseRedirect(reverse("chats:viewchat", chat_id=chat.pk)
			else:
				render(request, "chats/create.html", {"form": ChatForm(), "error": "All fields are required :("})
		form = ChatForm()
		return render(request, "chats/create.html", {"form": form})
	else:
		return HttpResponseRedirect(reverse("chats:login"))
	
def new_post(request, chat_id):
	if request.user.is_authenticated:
		chat = Chat.objects.filter(pk=chat_id)
		if ChatPerm.objects.filter(user=request.user).filter(chat=chat):
			if request.method == "post":
				form = PostForm(request.POST)
				if form.is_valid():
					post = Post(owner = request.user, body = form.cleaned_data["body"], date = date.today(), chat = chat)
					post.save()
					return HttpResponseRedirect(reverse("chats:viewchat", chat_id=chat_id))
				else:
					return HttpResponseRedirect(reverse("chats:viewchat", chat_id=chat_id))
			else:
				return HttpResponse("What are you doing here?<br>Oh I think you know.<br>Oh I really do-on't.")
		else:
			return HttpResponse("You not allowed to enter page bye now")
	else:
		return HttpResponseRedirect(reverse("chats:login"))
	
def invite(request, chat_id):
	if request.user.is_authenticated:
		chat = Chat.objects.filter(pk=chat_id)
		if ChatPerm.objects.filter(user=request.user).filter(chat=chat):
			if request.method == "post":
				pass


































