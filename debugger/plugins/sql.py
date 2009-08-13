import os
import SocketServer
import time
import datetime
import traceback
import django
from django.conf import settings
from django.db import connection
from django.db.backends import util
from django.template.loader import render_to_string
from django.utils import simplejson
from django.utils.encoding import force_unicode
from django.utils.hashcompat import sha_constructor

from debugger.plugins import DebuggerPlugin
from debugger.models import Sql, Request

# Figure out some paths
django_path = os.path.realpath(os.path.dirname(django.__file__))
socketserver_path = os.path.realpath(os.path.dirname(SocketServer.__file__))

def tidy_stacktrace(strace):
    """
    Clean up stacktrace and remove all entries that:
    1. Are part of Django (except contrib apps)
    2. Are part of SocketServer (used by Django's dev server)
    3. Are the last entry (which is part of our stacktracing code)
    """
    trace = []
    for s in strace[:-1]:
        s_path = os.path.realpath(s[0])
        if django_path in s_path and not 'django/contrib' in s_path:
            continue
        if socketserver_path in s_path:
            continue
        trace.append((s[0], s[1], s[2], s[3]))
    return trace

class DatabaseStatTracker(util.CursorDebugWrapper):
    """
    Replacement for CursorDebugWrapper which stores additional information
    in `connection.queries`.
    """
    def execute(self, sql, params=()):
        start = time.time()
        try:
            return self.cursor.execute(sql, params)
        finally:
            stop = time.time()
            stacktrace = tidy_stacktrace(traceback.extract_stack())
            _params = ''
            try:
                _params = simplejson.dumps([force_unicode(x) for x in params])
            except TypeError:
                pass # object not JSON serializable
            # We keep `sql` to maintain backwards compatibility
            self.db.queries.append({
                'sql': self.db.ops.last_executed_query(self.cursor, sql, params),
                'time': (stop - start) * 1000, # convert to ms
                'raw_sql': sql,
                'params': _params,
                'stacktrace': stacktrace,
                'timestamp': datetime.datetime.now(),
            })
util.CursorDebugWrapper = DatabaseStatTracker

class SQL(DebuggerPlugin):
    """
    Plugin that stores SQL information.
    """
    def __init__(self):
        self._offset = len(connection.queries)

    def process_response(self, db_request, request, response):
        for query in connection.queries[self._offset:]:
            Sql(
                request=db_request,
                elapsed_time=query['time'],
                sql=query['raw_sql'],
                executed_sql=query['sql'],
                stacktrace=simplejson.dumps(query['stacktrace']),
                timestamp=query['timestamp'],
            ).save()

