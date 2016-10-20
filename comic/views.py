
from math import floor
from random import random

from django.core.urlresolvers import reverse
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Comic

# Create your views here.
def view(request, num=None):
	all_comics = Comic.objects.all()
	if num is None:
		num = len(all_comics)
	else:
		num = int(num)
	comic = all_comics.get(cn=num)
	return render(request, "comic/viewit.html", {"comic": comic, "num_comics": len(all_comics)})
	
def random_comic(request):
	all_comics = Comic.objects.all()
	num = floor(random() * len(all_comics)) + 1
	return HttpResponseRedirect(reverse('comic:view', args=[str(num)]))