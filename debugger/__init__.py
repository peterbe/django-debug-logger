VERSION = (0, 7, 0)
__version__ = '.'.join(map(str, VERSION))

class Debugger(object):

    def __init__(self):
        self.plugins = []
        # Override this tuple by copying to settings.py as `DEBUGGER_PLUGINS`
        self.default_plugins = (
            'debugger.plugins.sql.SQL',
        )
        self.load_plugins()

    def load_plugins(self):
        """
        Populate debugger plugins
        """
        from django.conf import settings
        from django.core import exceptions

        # Check if settings has a DEBUGGER_PLUGINS, otherwise use default
        if hasattr(settings, 'DEBUGGER_PLUGINS'):
            self.default_plugins = settings.DEBUGGER_PLUGINS

        for plugin_path in self.default_plugins:
            try:
                dot = plugin_path.rindex('.')
            except ValueError:
                raise exceptions.ImproperlyConfigured, '%s isn\'t a debugger plugin module' % plugin_path
            plugin_module, plugin_classname = plugin_path[:dot], plugin_path[dot+1:]
            try:
                mod = __import__(plugin_module, {}, {}, [''])
            except ImportError, e:
                raise exceptions.ImproperlyConfigured, 'Error importing debugger plugin %s: "%s"' % (plugin_module, e)
            try:
                plugin_class = getattr(mod, plugin_classname)
            except AttributeError:
                raise exceptions.ImproperlyConfigured, 'Debugger Plugin module "%s" does not define a "%s" class' % (plugin_module, plugin_classname)

            try:
                plugin_instance = plugin_class()
            except:
                print plugin_class
                raise # Bubble up problem loading plugin

            self.plugins.append(plugin_instance)

            # TODO: Consider some sort of on-load clear tables ability?
