from online_journal_app.models import *
from django.utils import timezone
import re

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

'''entryFilter will return all entries filtered by any supplied parameters.'''
def entryFilter(author_id = None, datestart = None, dateend = None, taglist = None):
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
	return sorted(foundEntries, key = lambda x: x.pub_date)

'''entrySearch will search through the text relevant to each Entry and return a list of results
sorted by relevance.'''
def entrySearch(searchString, author_id = None):
	results = [[e, 0] for e in Entry.objects.all()]
	if author_id:
		_author = getAuthor(author_id)
		if not _author:
			return []
		results = [e for e in results if e[0].author == _author]
	searches = searchString.split()
	for entscr in results:
		entscr[1] = score(entscr[0], searches)
	results = sorted(results, key=lambda es: -es[1])
	return [entry[0] for entry in results if entry[1] > 0]

'''score will assign a score to a given Entry based on the list of search strings'''
def score(entry, searches):
	score = 0
	entryText = [entry.content, entry.title, entry.author.name] + [t.name for t in entry.tag_set.all()]
	for search in searches:
		tempScore = 1000
		p = re.compile(search, re.IGNORECASE)
		for s in entryText:
			tempScore += len(p.findall(s))
		if tempScore > 1000:
			score += tempScore
	return score

'''getTagList returns a list(strings) of distinct tag names'''
def getTagList(author_id):
	_author = getAuthor(author_id)
	if not _author:
		return []
	entries = _author.entry_set.all()
	tags = set([])
	for entry in entries:
		tags = set(tags) | set([t.name for t in entry.tag_set.all()])
	return list(tags)

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

'''updateAuthor will edit (if author_id is supplied) or create (if not) an author,
	set the properties to the parameters supplied and update the database.
	When done, updateAuthor will return the id of the newly created or edited author.'''
def updateAuthor(author_id = None, auth_identifier = None, name = None):
	_author = Author()
	if author_id:
		_author = Author.objects.get(id = author_id)
	else:
		if not (auth_identifier and name):
			return 0
	if auth_identifier:
		_author.auth_identifier = auth_identifier
	if name:
		_author.name = name
	_author.save()
	return _author.id

'''updateTag will edit (if tag_id is supplied) or create (if not) an tag,
	set the properties to the parameters supplied and update the database.
	When done, updateTag will return the id of the newly created or edited tag.'''
def updateTag(tag_id = None, name = None, entry = None):
	_tag = Tag()
	if tag_id:
		_tag = Tag.objects.get(id = tag_id)
	else:
		if not (name and entry):
			return 0
	if name:
		_tag.name = name
	if entry:
		_tag.entry = entry
	_tag.save()
	return _tag.id

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

'''deleteAuthor deletes an author and all child objects. In the future, these deletes may be replaced with soft delete
	flags instead- for now, however, this will be a permanent delete for simplicity's sake.
	Unlike my other delete functions, this will use the standard author identifier, rather than the id; this way,
	I can try for consistency across my functions and avoid requiring developers to find an author id that they would
	otherwise not need.'''
def deleteAuthor(identifier):
	_author = getAuthor(identifier)
	for _entry in _author.entry_set.all():
		for _tag in _entry.tag_set.all():
			_tag.delete()
		_entry.delete()
	_author.delete()

'''deleteEntry will delete an Entry and all child objects.'''
def deleteEntry(entry_id):
	_entry = Entry.objects.get(id = entry_id)
	for _tag in _entry.tag_set.all():
		_tag.delete()
	_entry.delete()

'''deleteTag will delete a Tag.'''
def deleteTag(tag_id):
	_tag = Tag.objects.get(id = tag_id)
	_tag.delete()
