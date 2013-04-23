from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Picture(models.Model):
	name = models.CharField(max_length=255)
	author = models.ForeignKey(User)
	projects = models.ManyToManyField('Project')
	uploaded = models.DateTimeField(auto_now=True)
	picture = models.ImageField(upload_to='pictures')
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image_type = models.CharField(max_length=5, default='')
	image_size = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
