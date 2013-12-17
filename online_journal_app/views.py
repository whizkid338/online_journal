from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.dateparse import *
from django.views.decorators.csrf import *
from online_journal_app.queries import *

from online_journal_app.models import Author, Entry, Tag
from online_journal_app.forms import *
from rest_framework import viewsets
from online_journal_app.serializers import AuthorSerializer, EntrySerializer, TagSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# Create your views here.

def index(request):
    return render_to_response('index.html')

def base(request):
    username = "Sign in"
    # process username here from query
    return render_to_response('base.html', {'username': username})

def entry(request):
    username = "Sign in"
    # process username here from query
    return render_to_response('entry.html', {'username': username})

def view(request):
    username = "Sign in"
    entry = entryFilter()
    # process username here from query
    return render_to_response('view.html', {'username': username, 'entries': entry})

def submitEntry(request):
	entryId = 0
	if request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
				title = form.cleaned_data['title']
				pub_date = form.cleaned_data['pub_date']
				pub_date = parse_datetime(pub_date)
				content = form.cleaned_data['content']
				entryId = updateEntry(author_id=1, title=title, content=content, pub_date=pub_date)
	else:
		form = EntryForm()
	return render_to_response('view.html', form, entryId)

def find(request):
    username = "Sign in"
    # process username here from query
    # entrySearch(request.authorID)
    return render_to_response('find.html', {'username': username})
