from online_journal_app.models import *
from django.utils import timezone

# def getEntriesByDate(author_id, date):
# 	auth = getAuthor(author_id)
# 	return Entry.objects.filter(pub_date__gte = date,
# 								pub_date__lt = date + datetime.timedelta(1),
# 								author = auth)

# def getEntriesByTag(author_id, name):
# 	auth = getAuthor(author_id)
# 	return [t.entry for t in Tag.objects.filter(name = name) if t.entry.author == auth]

# def getEntryTags(entry_id):
# 	return list(set([t.name for t in Entry.objects.get(id = entry_id).tag_set.all()]))

'''entrySearch will return all entries filtered by any supplied parameters.'''
def entrySearch(author_id = None, datestart = None, dateend = None, taglist = None):
	foundEntries = Entry.objects.all()

	if author_id:
		_author = getAuthor(author_id)
		if not _author:
			return []
		foundEntries = [entry for entry in foundEntries if entry.author == _author]

	if datestart:
		foundEntries = [entry for entry in foundEntries if entry.pub_date > datestart]

	if dateend:
		foundEntries = [entry for entry in foundEntries if entry.pub_date < dateend]

	if taglist:
		foundEntries = [entry for entry in foundEntries if set(taglist).issubset(set([tag.name for tag in entry.tag_set.all()]))]

	return foundEntries

'''getTagList returns a list(strings) of distinct tag names'''
def getTagList(author_id):
	_author = getAuthor(author_id)
	if not _author:
		return []
	entries = _author.entry_set.all()
	tags = []

	for entry in entries:
		tags = list(set(tags) | set([t.name for t in entry.tag_set.all()]))

	return tags

'''updateEntry will edit (if entry_id is supplied) or create (if not) an entry,
	set the properties to the parameters supplied and update the database.
	When done, updateEntry will return the id of the newly created or edited record.'''
def updateEntry(author_id, entry_id = None, title = None, content = None, pub_date = None):
	_entry = Entry()
	_author = getAuthor(author_id)
	if not _author:
		return 0

	if entry_id:

		try:
			_entry = Entry.objects.get(id = entry_id)
		except:
			return 0

		# Check for invalid author; do not allow anyone other than the original author to edit an Entry
		if _entry.author != _author:
			return 0
	else:
		_entry.author = _author
		_entry.pub_date = timezone.now()

	if title:
		_entry.title = title

	if content:
		_entry.content = content

	if pub_date:
		_entry.pub_date = pub_date

	_entry.save()
	return _entry.id

'''getEntry will return the entry by id. If an author is specified, getEntry will verify that the author matches;
	otherwise, it will return None.'''
def getEntry(entry_id, author_id = None):
	try:
		_entry = Entry.objects.get(id = entry_id)
		if author_id and _entry.author != getAuthor(author_id):
			return None
		return _entry
	except:
		return None

'''getAuthor is a convenient way for us to use some identifier to select an existing author.'''
def getAuthor(identifier):
	try:
		return Author.objects.get(auth_identifier = identifier)
	except:
		return None
