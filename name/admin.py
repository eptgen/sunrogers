from django.contrib import admin

from .models import NameModel as Name

# Register your models here.

class NameAdmin(admin.ModelAdmin):
	fields = ["name", "email", "age"]
	list_display = ("name", "email", "age")

admin.site.register(Name, NameAdmin)