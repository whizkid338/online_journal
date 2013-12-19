import os, sys
sys.path.append('/home/ubuntu/online_journal')
os.environ['DJANGO_SETTINGS_MODULE'] = 'online_journal.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
