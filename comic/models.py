from django.db import models

def cn_default():
	return len(Comic.objects.all())+1

# Create your models here.
class Comic(models.Model):
	img = models.ImageField(upload_to="comics/")
	title = models.CharField(max_length=100)
	alt = models.CharField(max_length=300)
	date_done = models.DateField()
	cn = models.IntegerField(default=cn_default)
	