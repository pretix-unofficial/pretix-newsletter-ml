from django.apps import AppConfig


class PluginApp(AppConfig):
    name = 'pretix_newsletter_ml'
    verbose_name = 'pretix newsletter integration for mailing lists'

    class PretixPluginMeta:
        name = 'pretix newsletter integration for mailing lists'
        author = 'Raphael Michel'
        description = 'pretix newsletter integration for mailing lists'
        visible = True
        version = '1.3.1'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_newsletter_ml.PluginApp'
