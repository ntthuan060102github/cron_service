from django.apps import AppConfig

class DjangoAppConfig(AppConfig):
    name = 'django_app'
    default_auto_field = 'django.db.models.BigAutoField'
    service_name_abbreviation = "mypt-cron-api"
    service_name_semantic = "My PT - Cron Management Service"
    service_version = "1.0.0"
    service_version_abbreviation = "v1"
    api_prefix = f"{service_name_abbreviation}/{service_version_abbreviation}"
    session_cache_database = 15
    cache_partition = "cron_service"

    # def ready(self):
    #     import django_app.signals.survey_schedule
