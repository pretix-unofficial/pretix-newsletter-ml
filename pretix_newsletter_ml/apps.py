from django.apps import AppConfig
from . import __version__


class PluginApp(AppConfig):
    name = 'pretix_newsletter_ml'
    verbose_name = 'pretix newsletter integration for mailing lists'

    class PretixPluginMeta:
        name = 'pretix newsletter integration for mailing lists'
        author = 'Raphael Michel'
        description = 'pretix newsletter integration for mailing lists'
        visible = True
        version = __version__

    def ready(self):
        from . import signals  # NOQA


