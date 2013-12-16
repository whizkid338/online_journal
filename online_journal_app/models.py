from django.db import models

# Create your models here.
class Author(models.Model):
	def __unicode__(self):
		return self.name
	
	auth_identifier = models.CharField(max_length=255)
	name = models.CharField(max_length=255)

class Entry(models.Model):
	def __unicode__(self):
		return self.title

	author = models.ForeignKey(Author)
	title = models.CharField(max_length=255)
	content = models.TextField()
	pub_date = models.DateTimeField('Date of Entry')
	last_edit = models.DateTimeField('Most Recent Edit')

class Tag(models.Model):
	def __unicode__(self):
		return self.name

	entry = models.ForeignKey(Entry)
	name = models.CharField(max_length=50)
