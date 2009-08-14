===================
Django Debug Logger
===================

The Django Debug Logger is a configurable set of plugins that log various debugging
information about the current request/response to the database, and views to
display those logs in various useful ways.

Currently, the following plugins are included:

- SQL queries including time to execute and traceback to where the SQL
  originated

If you have ideas for other plugins please let us know.

Installation
============

#. Add the `debug_logger` directory to your Python path.

#. Add the following middleware to your project's `settings.py` file:

	``'debug_logger.middleware.DebugLoggerMiddleware',``

   Tying into middleware allows each plugin to be instantiated on request and
   database logging to happen on response.

#. Add `debug_logger` to your `INSTALLED_APPS` setting.

#. Run `python manage.py syncdb` to install the database tables.

Configuration
=============

The Django Debug Logger has one setting that can be set in `settings.py`:

#. Optional: Add a tuple called `DEBUG_LOGGER_PLUGINS` to your ``settings.py``
   file that specifies the full Python path to the plugin that you want
   included.  This setting looks very much like the `MIDDLEWARE_CLASSES`
   setting.  For example::

	DEBUG_LOGGER_PLUGINS = (
	    'debug_logger.plugins.sql.SQL',
	)

   If you have custom plugins you can include them in this way -- just provide
   the full Python path to your plugins.

TODOs and BUGS
==============
See: http://github.com/robhudson/django-debug-logger/issues

STATUS
======
Currently very much in the proof of concept phase.  While it's working and
showing good signs there is much to do with making the "plugins" more
"pluggable".

Help or ideas are appreciated.
