===============
Django Debugger
===============

The Django Debugger is a configurable set of plugins that log various debugging
information about the current request/response to the database, and views to
display those logs in various useful ways.

Currently, the following plugins are included:

- SQL queries including time to execute and traceback to where the SQL
  originated

If you have ideas for other panels please let us know.

Installation
============

#. Add the `debugger` directory to your Python path.

#. Add the following middleware to your project's `settings.py` file:

	``'debugger.middleware.DebuggerMiddleware',``

   Tying into middleware allows each plugin to be instantiated on request and
   database logging to happen on response.

#. Add `debugger` to your `INSTALLED_APPS` setting.

#. Run `python manage.py syncdb` to install the database tables.

Configuration
=============

The Django Debugger has two settings that can be set in `settings.py`:

#. Optional: Add a tuple called `DEBUGGER_PLUGINS` to your ``settings.py`` file
   that specifies the full Python path to the plugin that you want included.
   This setting looks very much like the `MIDDLEWARE_CLASSES` setting.  For
   example::

	DEBUGGER_PLUGINS = (
	    'debugger.plugins.sql.SQL',
	)

   If you have custom panels you can include them in this way -- just provide
   the full Python path to your panel.

TODOs and BUGS
==============
See: http://github.com/robhudson/django-debugger/issues
