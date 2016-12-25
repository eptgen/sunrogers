from io import BytesIO

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse
from django.utils.encoding import smart_str

from .forms import ChristmasForm

def index(request):
	return render(request, "ebdjango/index.html", {})
	
def bub(request):
	return render(request, "ebdjango/bub.html", {})
	
def bump(request):
	return HttpResponse("<title>Bump</title>bump")
	
def isfat(request):
	return HttpResponse("<title>Fat?</title>Calculating...<br />Result: yes")
	
def php(request):
	return render(request, "ebdjango/thing.php", {})
	
def cd(request):
	return HttpResponse("")
	
def mixtape(request):
	response = HttpResponse(content_type="audio/mpeg3")
	response["Content-Disposition"] = "attachment; filename=\"%s\"" % smart_str("ebdjango/do-what-i-want.mp3")
	"""
	print(static("ebdjango/do-what-i-want.mp3"))
	response["X-Sendfile"] = smart_str(static("ebdjango/do-what-i-want.mp3"))
	"""
	return response
	
def verification(request):
	return render(request, "ebdjango/google503cd29fc95f3756.html", {})
	
def do_404(request):
	return HttpResponse("<h1>What are you even trying to do?</h1>")
	
def favicon(request):
	return HttpResponseRedirect(static("ebdjango/favicon.png"))
	
def christmas_home(request):
	return render(request, "ebdjango/chome.html", {})
	
def christmas_inputs(request):
	if request.method == "POST":
		form = ChristmasForm(request.POST)
		if form.is_valid():
			if form.cleaned_data["one"].lower() == "run" and form.cleaned_data["two"].lower() == "away" and form.cleaned_data["three"].lower() == "now":
				return HttpResponse("<h1>MERRY CHRISTMAS!!!!!!!!!!!</h1><p>Where am I? I guess I've gone back to nature...</p>")
		else:
			return HttpResponseRedirect(reverse("christmasinputs"))
	form = ChristmasForm()
	return render(request, "ebdjango/cinputs.html", {"form": form})


































