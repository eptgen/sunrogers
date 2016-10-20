from django.contrib import admin

from .models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	fields = ["title", "pub_date", "post_text"]
	list_display = ("title", "pub_date", "post_text")
	
admin.site.register(BlogPost, BlogPostAdmin)