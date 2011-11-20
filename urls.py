from django.conf.urls.defaults import *
from django.contrib import admin
import os

admin.autodiscover()

urlpatterns = patterns('mark.views',
    url(r'^$', 'show'),
    url(r'^put/$', 'put'),
    url(r'^lab/add/$', 'add_lab', name='add_lab'),
    url(r'^student/add/$', 'add_student', name='add_student'),
    url(r'^student/del/(\d+)/$', 'del_student', name='del_student'),
)
(r'^admin/', include(admin.site.urls)),

# DEBUG ONLY
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': os.path.join(os.path.dirname(__file__), 'media'),}),
)