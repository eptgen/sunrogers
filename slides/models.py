from django.db import models

# Create your models here.

class Slide(models.Model):
	img = models.ImageField(upload_to="slides/")

class Show(models.Model):
	title = models.CharField(max_length=100)
	slides = models.ForeignKey(Slide)
	num = models.IntegerField(default=0)