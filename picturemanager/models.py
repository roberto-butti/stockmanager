from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Picture(models.Model):
	name = models.CharField(max_length=255)
	author = models.ForeignKey(User)
	projects = models.ManyToManyField('Project')
	uploaded = models.DateTimeField(auto_now=True)
	picture = models.ImageField(upload_to='pictures')
	exif = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class Project(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
