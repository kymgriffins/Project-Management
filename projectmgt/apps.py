from django.apps import AppConfig


class ProjectmgtConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "projectmgt"
    def ready(self):
        import projectmgt.signals
