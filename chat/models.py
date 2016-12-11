from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=1000)
	create_date = models.DateField()
	
class Post(models.Model):
	owner = models.ForeignKey(User)
	body = models.CharField(max_length=1000)
	date = models.DateTimeField()
	chat = models.ForeignKey(Chat)
	
class ChatPerm(models.Model):
	user = models.ForeignKey(User)
	chat = models.ForeignKey(Chat)


































