from django.contrib import admin

from .models import Slide, Show

# Register your models here.

class SlideInline(admin.TabularInline):
	model = Slide
	extra = 3
	
class ShowAdmin(admin.ModelAdmin):
	inlines = [SlideInline]
	
admin.site.register(Show, ShowAdmin)
