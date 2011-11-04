from django.conf.urls.defaults import *
from mark.views import *
from django.contrib import admin
import os

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', show),
    (r'^put/$', put),
    (r'^students/add/$', stud_add),
    (r'^students/del/(\d+)/$', stud_del),
    (r'^admin/', include(admin.site.urls)),
)

# DEBUG ONLY
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': os.path.join(os.path.dirname(__file__), 'media'),}),
)