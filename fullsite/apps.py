from django.apps import AppConfig


class FullsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fullsite'
    
    def ready(self) -> None:
       from fullsite import signals