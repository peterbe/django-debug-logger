"""
Debug Logger Middleware
"""
import datetime
import os

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.encoding import smart_unicode
from django.conf.urls.defaults import include, patterns

from debug_logger import DebugLogger
from debug_logger.models import Request

# TODO: Consider setting request model obj via signals request_started, request_finished
# TODO: Make this configurable
DEBUG_LOGGER_IGNORE_URLS = (
    '/media',
    '/admin',
    '/debug_logger',
)
DEBUG_LOGGER_ALLOWABLE_STATUS_CODES = (
    200,
    301, # permanent redirect
    302, # redirect
    304, # response not modified
)


class DebugLoggerMiddleware(object):
    """
    Middleware to set up Debug Logger on incoming request and write out debug logs
    on response.
    """
    def __init__(self):
        self.debug_logger = DebugLogger()
        self.db_request = None

    def do_log(self, request):
        if not settings.DEBUG:
            return False
        # TODO: if this request is part of a debug_logger url
        # TODO:     return False
        for url in DEBUG_LOGGER_IGNORE_URLS:
            if request.path.startswith(url):
                return False
        return True

    def process_request(self, request):
        # Each request, determine if we should log this request
        if self.do_log(request):
            self._do_log = True
        else:
            self._do_log = False
        if self._do_log:
            self.db_request = Request(
                timestamp=datetime.datetime.now,
                method=request.method,
                absolute_path=request.build_absolute_uri(),
                # We don't know response code and size at this point
            )
            for plugin in self.debug_logger.plugins:
                plugin.process_request(request)
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        if self._do_log:
            for plugin in self.debug_logger.plugins:
                plugin.process_view(request, view_func, view_args, view_kwargs)

    def process_response(self, request, response):
        if not self._do_log:
            return response
        if response.status_code not in DEBUG_LOGGER_ALLOWABLE_STATUS_CODES:
            return response
        # Debug Logger processing
        self.db_request.status_code = response.status_code
        # TODO: self.db_request.response_size = 
        self.db_request.save()
        for plugin in self.debug_logger.plugins:
            plugin.process_response(self.db_request, request, response)
        return response
