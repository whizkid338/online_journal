from django import forms
from django.forms import ModelForm
from online_journal_app.models import *

class EntryForm(ModelForm):
	class Meta:
		model = Entry
		exclude = ["author"]
