from django_app.views.cron_management import CronManagementView
from rest_framework_nested import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register("cron", CronManagementView, basename='cron')

urls = router.urls