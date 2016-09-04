from django.conf.urls.defaults import *
from django.utils.translation import ugettext as _
from django.conf import settings

#urlpatterns = patterns('',
#    (r'', include('forum.urls')),
#)
#
#if 'rosetta' in settings.INSTALLED_APPS:
#    urlpatterns = patterns('',
#        url(r'^rosetta/', include('rosetta.urls')),
#    ) + urlpatterns
#
#handler404 = 'forum.views.meta.page'
#handler500 = 'forum.views.meta.error_handler'


#https://github.com/OSQA/osqa/blob/master/urls.py
urlpatterns = patterns('',
    (r'^%s' % settings.FORUM_SCRIPT_ALIAS, include('forum.urls')),
)
