from django.conf.urls.defaults import *
from mark.views import *
import os

urlpatterns = patterns('',
    (r'^$', show),
    (r'^put/$', put),
    (r'^students/add/$', stud_add),
)

# DEBUG ONLY
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': os.path.join(os.path.dirname(__file__), 'media'),}),
)