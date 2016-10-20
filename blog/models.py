from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateField()
	post_text = models.FileField(upload_to="blogposts/")
	def body(self):
		with open(self.post_text.path) as f:
			return f.read().replace("\n", "<br>")
			
class Tag(models.Model):
	val = models.CharField(max_length=30)
	post = models.ForeignKey(BlogPost)