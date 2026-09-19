from django.apps import AppConfig


class DecorationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Decoration'

    def ready(self):
        import Decoration.signals  # Import the signals here


