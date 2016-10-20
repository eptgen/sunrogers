from django.db import models

# Create your models here.

class NameModel(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=40)
	age = models.IntegerField()