import json

from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .models import Slide, Show

# Create your views here.

slide = 0
show = 0
with open("../slidestate", "r") as f:
	data = json.loads(f.read())
	slide = data["slide"]
	show = data["show"]
	
def update():
	with open("slidestate", "w") as f:
		f.write(json.dumps({"slide": slide, "show": show}))
		
def next_slide(request):
	global slide
	current_slide = Slide.objects.get(pk=slide)
	current_show = Show.objects.get(pk=show)
	new_slide = Slide.objects.filter(num=current_slide.num + 1, show=current_show)
	if new_slide:
		slide = new_slide[0].pk
		update()
	return HttpResponse("success")
	
def prev_slide(request):
	global slide
	current_slide = Slide.objects.get(pk=slide)
	current_show = Show.objects.get(pk=show)
	if (current_slide.num > 1):
		new_slide = Slide.objects.get(num=current_slide.num - 1, show=current_show)
		slide = new_slide.pk
		update()
	return HttpResponse("success")

def home(request):
	mslide = Slide.objects.get(pk=slide)
	url = reverse("slides:data")
	return render(request, "slides/index.html", context={"slide": mslide, "url": url})
	
def change_show(request):
	global show, slide
	show = int(dict(request.GET)["show"][0])
	slide = Slide.objects.get(show=show, num=1)
	update()
	return HttpResponse("success")
	
def change_slide(request):
	global slide
	slide = int(dict(request.GET)["slide"])
	update()
	return HttpResponse("success")
	
def data(request):
	mslide = Slide.objects.get(pk=slide)
	return HttpResponse(mslide.img.url)


































