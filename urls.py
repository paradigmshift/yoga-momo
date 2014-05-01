from django.conf.urls.defaults import patterns, include, url
from articles.models import Entry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yoga_momo.views.home', name='home'),
    # url(r'^yoga_momo/', include('yoga_momo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        { 'document_root': '/home/mo/projects/yoga_momo/media'}),
                       (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                        { 'document_root': '/home/mo/installed-apps/tinymce/tinymce/jscripts/tiny_mce'}),
                       (r'^$', 'django.views.generic.simple.redirect_to', {'url':'/news/'}),
                       (r'^contact/$', include('send-mail.urls')),
                       (r'^weblog/', include('articles.urls')),
                       (r'', include('django.contrib.flatpages.urls')),
)
