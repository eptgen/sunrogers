
from django.http import HttpResponse
from django.db.models import F
from django.shortcuts import render

from .models import BlogPost

# Create your views here.

months = [None] + "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")

def blog(request, year=None, month=None):
	posts = BlogPost.objects.order_by(F("pk").desc())
	max_year = posts[0].pub_date.year
	max_month = posts[0].pub_date.month
	print("year", year)
	print("month", month)
	if year is None:
		year = max_year
		month = max_month
	min_year = posts[len(posts) - 1].pub_date.year		# What do you mean, "negative indexing is not supported"?
	min_month = posts[len(posts) - 1].pub_date.month
	posts = posts.filter(pub_date__year=year, pub_date__month=month)
	archives = []
	for i in range(min_year, max_year+1):
		begin = 1						#
		end = 13						#
		if i == min_year:				#
			begin = min_month			# Looks confusing, but just to make sure the archives start at the right time
		if i == max_year:				#
			end = max_month + 1			#
		for j in range(begin, end):		#
			to_add = {}
			to_add["year"] = str(i)
			to_add["month"] = months[j]
			to_add["nmonth"] = str(j)
			archives.append(to_add)
	return render(request, 'blog/index.html', {"posts": posts, "archives": archives, "year": str(year), "month": str(month)})
	
def subscribe(request):
	return HttpResponse("hi")


































