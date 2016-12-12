from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

# Create your views here.

message = ""
with open("message", "r") as f:
	message = str(f.read())

def update_file():
	with open("message", "w") as f:
		f.write(message)

def pretty(request):
	return render(request, "broadcast/pretty.html", {"url": reverse("broadcast:get"), "message": message})
	
def gett(request):
	return HttpResponse(message)
	
def change(request):
	global message
	data = dict(request.GET)
	if str(data["code"]) == "314159" or data["code"][0] == "314159":
		message = data["message"][0]
		update_file()
		return HttpResponse("success: " + message)
	else:
		return HttpResponse("erorr: wrong code: " + str(data["code"]))


































