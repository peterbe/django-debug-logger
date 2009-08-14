"""
URLpatterns for the debug_logger.
"""
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^$', 'debug_logger.views.index', name='debug_logger_index'),
    url('^sql/(?P<request_id>\d+)$', 'debug_logger.views.sql_list', name='debug_logger_sql_list'),
)
