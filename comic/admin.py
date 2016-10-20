from django.contrib import admin

from .models import Comic

# Register your models here.
class ComicAdmin(admin.ModelAdmin):
	fields = ["img", "title", "alt", "date_done", "cn"]
	list_display = ("img", "title", "alt", "date_done", "cn")
	
admin.site.register(Comic, ComicAdmin)