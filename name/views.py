
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .forms import NameForm
from .models import NameModel

def data_for(form, *values):
	result = []
	for i in values:
		result.append(form.cleaned_data[i])
	return result

# Create your views here.
def index(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			name, email, age = data_for(form, "name", "email", "age")
			name_model = NameModel(name=name, email=email, age=age)
			name_model.save()
			# print(reverse("name:done"))
			return HttpResponseRedirect(reverse("name:done"))
		else:
			return HttpReponse("NO")
	else:
		form = NameForm()
		return render(request, "name/form.html", context={"form": form})
			
def done(request):
	return HttpResponse("thanks, bye")
			