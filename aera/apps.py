from django.apps import AppConfig


class AeraConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aera"
    verbose_name = "ÆRA"
    is_modular = True
    root_url = "/AERA"
    icon = "⚙"
