import json

from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render

from .models import Slide

# Create your views here.

slide = 0
show = 0
with open("slidestate", "r") as f:
	data = json.parse(f.read())
	slide = data["slide"]
	show = data["show"]
	
def update():
	with open("slidestate", "w") as f:
		f.write(json.stringify({"slide": slide, "show": show}))
		
def next_slide(request):
	pass
	
def prev_slide(request):
	pass

def home(request):
	return render(request, "slides/index.html", {})
	
def change_show(request):
	show = int(dict(request.GET)["show"])
	
def change_slide(request):
	slide = int(dict(request.GET)["slide"])
	
def data(request):
	mslide = slide.objects.get(pk=slide)
	return HttpResponse(mslide.url())


































