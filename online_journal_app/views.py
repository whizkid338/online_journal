from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from online_journal_app.queries import *


# Create your views here.

def index(request):
    return render_to_response('index.html')

def base(request):
    return render_to_response('base.html')

def entry(request):
    return render_to_response('entry.html')

def view(request):
    return render_to_response('view.html')

def find(request):
    # entrySearch(request.authorID)
    return render_to_response('find.html')
