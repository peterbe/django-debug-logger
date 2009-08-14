"""
URLpatterns for the debugger.
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^$', 'debugger.views.index', name='debugger_index'),
    url('^sql/(?P<request_id>\d+)$', 'debugger.views.sql_list', name='debugger_sql_list'),
)
