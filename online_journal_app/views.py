from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from online_journal_app.queries import *


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
    # process username here from query
    return render_to_response('view.html', {'username': username})

def find(request):
    username = "Sign in"
    # process username here from query
    # entrySearch(request.authorID)
    return render_to_response('find.html', {'username': username})
