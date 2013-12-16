from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'online_journal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'online_journal_app.views.index'),
    url(r'^index', 'online_journal_app.views.index'),
    url(r'^base', 'online_journal_app.views.base'),
    url(r'^entry', 'online_journal_app.views.entry'),
    url(r'^view', 'online_journal_app.views.view'),
    url(r'^find', 'online_journal_app.views.find'),
)
