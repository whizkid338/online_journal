from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from online_journal_app import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'entries', views.EntryViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'online_journal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rest/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'online_journal_app.views.index'),
    url(r'^index', 'online_journal_app.views.index'),
    url(r'^base', 'online_journal_app.views.base'),
    url(r'^entry', 'online_journal_app.views.entry'),
    url(r'^prevEntry', 'online_journal_app.views.prevEntry'),
    url(r'^nextEntry', 'online_journal_app.views.nextEntry'),
    url(r'^submitEntry', 'online_journal_app.views.submitEntry'),
    url(r'^view', 'online_journal_app.views.view'),
    url(r'^find', 'online_journal_app.views.find'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login', 'online_journal_app.views.login_page'),
    url(r'^authorize', 'online_journal_app.views.authorize'),
    url(r'^signup_page', 'online_journal_app.views.signup_page'),
    url(r'^createUser', 'online_journal_app.views.createUser'),
    url(r'^logout', 'online_journal_app.views.logout_view'),
) + static('/' + settings.STATIC_URL, document_root=settings.STATIC_ROOT)
