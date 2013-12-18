from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from online_journal_app.queries import *
from django.http import HttpResponse

from online_journal_app.models import Author, Entry, Tag
from rest_framework import viewsets
from online_journal_app.serializers import AuthorSerializer, EntrySerializer, TagSerializer

from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    return render_to_response('base.html', {'username': username}, RequestContext(request))

def entry(request):
    # if request.user.is_authenticated():
    #     return HttpResponse("We're logged in")
    # else:
    #     return HttpResponse("Not logged in")

    username = "Sign in"
    # process username here from query
    return render_to_response('entry.html', {'username': username}, RequestContext(request))

def view(request):
    username = "Sign in"
    entry = entryFilter()
    # process username here from query
    return render_to_response('view.html', {'username': username, 'entries': entry}, RequestContext(request))

def find(request):
    username = "Sign in"
    # process username here from query
    # entrySearch(request.authorID)
    return render_to_response('find.html', {'username': username}, RequestContext(request))

def login_page(request):
    form = AuthenticationForm
    return render(request, 'login_page.html', {'form':form,})

def authorize(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            # return redirect('/internalURL/')
            return redirect('/entry/')
        else:
            return HttpResponse("You are in, but not active")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Bad username and password")

def signup_page(request):
    form = UserCreationForm
    return render(request, 'signup_page.html', {'form':form})

def createUser(request):
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    # check for same passwords
    if password1 != password2:
        return HttpResponse("Your two passwords were not the same")

    # check to see if username already exists
    try:
        user = User.objects.create_user(username)
    except:
        return HttpResponse("Sorry, that username already exists")

    # user is created...just need to set the password
    user.set_password(password1)
    user.save()

    return HttpResponse("Congrats %s, you are now in our database" % username)

def logout_view(request):
    logout(request)
    return redirect('/entry/')