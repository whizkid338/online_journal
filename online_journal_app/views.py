from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.dateparse import *
from dateutil.parser import *
from django.views.decorators.csrf import *
import django.utils.timezone
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
    return render_to_response('entry.html', {'username': username})

def view(request, entryId=None):
    username = "Sign in"
    entry = getEntry(entryId)
    # process username here from query
    return render_to_response('view.html', {'username': username, 'entry': entry})

def submitEntry(request):
	entryId = 0
	title = "This is a temp"
	pub_date = 12/12/12
	content = "Temp content"
	if 'title' in request.POST and request.POST['title']:
			title = request.POST['title']
	if 'date' in request.POST and request.POST['date']:
			pub_date = request.POST['date']
			pub_date = parse(pub_date)
	if 'content' in request.POST and request.POST['content']:
			content = request.POST['content']
	entryId = updateEntry(author_id=1, title=title, content=content, pub_date=pub_date)
	return view(request, entryId)

def find(request):
    username = "Sign in"
    # process username here from query
    # entrySearch(request.authorID)
    return render_to_response('find.html', {'username': username})
