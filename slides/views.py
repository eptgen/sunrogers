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
	current_slide = Slide.objects.get(pk=slide)
	new_slide = Slide.objects.get(pk=current_slide.num + 1)
	slide = new_slide.pk
	
def prev_slide(request):
	current_slide = Slide.objects.get(pk=slide)
	new_slide = Slide.objects.get(pk=current_slide.num - 1)
	slide = new_slide.pk

def home(request):
	return render(request, "slides/index.html", {})
	
def change_show(request):
	show = int(dict(request.GET)["show"])
	return HttpResponse("success")
	
def change_slide(request):
	slide = int(dict(request.GET)["slide"])
	return HttpResponse("success")
	
def data(request):
	mslide = Slide.objects.get(pk=slide)
	return HttpResponse(mslide.url())


































