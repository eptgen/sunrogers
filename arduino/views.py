from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import ArduinoForm

# Create your views here.
is_on = False

def do_light(data):
	global is_on
	print(data)
	if str(data["code"]) == "314159" or data["code"][0] == "314159":
		if data["val"] == "on":
			is_on = True
		elif data["val"] == "off":
			is_on = False
		elif data["val"] == "toggle":
			is_on = not is_on
		else: print("problem")
	else: print("problem")

def on_or_off():
	return "on" if is_on else "off"

def main(request):
	form = ArduinoForm()
	success = ""
	if request.method == "POST":
		form = ArduinoForm(request.POST)
		if form.is_valid():
			do_light(form.cleaned_data)
			success = "Light changed to " + on_or_off() + " successfully."
	return render(request, "arduino/index.html", {"form": form, "success": success})

def func_light(string):
	def result(request):
		if request.method == "GET":
			data = dict(request.GET)
			data["val"] = string
			do_light(data)
			return HttpResponse("success")
	return result
			
on = func_light("on")
off = func_light("off")
toggle = func_light("toggle")

def get(request):
	result = "on" if is_on else "off"
	return HttpResponse(result)


































