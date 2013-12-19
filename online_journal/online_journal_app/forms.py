from django import forms
from django.forms import ModelForm
from online_journal_app.models import *

class EntryForm(ModelForm):
	class Meta:
		model = Entry
		exclude = ["author"]

class FindForm(forms.Form):
	author_id = forms.CharField(required=False, max_length=100)
	datestart = forms.DateField(required=False)
	dateend = forms.DateField(required=False)
	tag = forms.CharField(required=False, max_length=100)

class SearchForm(forms.Form):
	author_id = forms.CharField(required=False, max_length=100)
	search = forms.CharField(max_length=100)
