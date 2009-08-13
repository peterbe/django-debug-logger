"""Base Debugger Plugin class"""

class DebuggerPlugin(object):
    """
    Base class for debugger plugins.
    """
    def __init__(self):
        pass

    # Standard middleware methods
    def process_request(self, request):
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        pass

    def process_response(self, db_request, request, response):
        """
        `db_request` is a `debugger.models.Request` object that you can use as
         a ForeignKey to your debugger models.  It will have been saved to the
         database when your plugin `process_response` method is called, and
         therefore, will have a primary key.
        """
        pass

