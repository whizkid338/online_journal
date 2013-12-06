from django.db import models

class Entries(models.Model):
    userId = models.CharField(max_length=255)
    date = models.DateField()
    modifiedDate = models.DateField()
    title = models.CharField(max_length=255)
    entryText = models.TextField()

class Users(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

class Tags(models.Model):
    userId = models.ForeignKey(Users)
    entryId = models.ForeignKey(Entries)
    tagName = models.CharField(max_length=255)
