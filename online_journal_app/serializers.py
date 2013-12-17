#from django.contrib.auth.models import Author, Entry, Tag
from online_journal_app.models import Author, Entry, Tag
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('auth_identifier', 'name')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ('author', 'title', 'content', 'pub_date', 'last_edit')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('entry', 'name')
