from django.db import models

# Create your models here.

class Show(models.Model):
	title = models.CharField(max_length=100)

class Slide(models.Model):
	img = models.ImageField(upload_to="slides/")
	show = models.ForeignKey(Show, default=None)
	num = models.IntegerField(default=0)