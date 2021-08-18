from django.apps import AppConfig


class QplotlyConfig(AppConfig):
    name = 'qplotly'
    verbose_name = 'Qplotly'

    def ready(self):

        # import signal handlers
        import qplotly.receivers

        # Register Layout buy QGS_APPLICATION
        from .utils import qplotly_layouts