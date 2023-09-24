from django_celery_beat.models import PeriodicTask
from django_app.serializers.periodic_task_serializer import PeriodicTaskSerializer
from django_app.app_management.app_messages import MessageManager
from app_core.views.common_view.common_view import CommonView
from app_core.views.common_view.components import (
    CreateModelComponent, 
    DeleteModelComponent, 
    UpdateModelComponent
)
from helpers.response import ResponseManager as Response

class CronManagementView(
        CommonView, 
        CreateModelComponent, 
        DeleteModelComponent, 
        UpdateModelComponent
    ):
    serializer_class = PeriodicTaskSerializer
    queryset = PeriodicTask.objects.all()
    messages = MessageManager.survey
        
    def destroy(self, request, pk):
        try:
            instance = PeriodicTask.objects.get(id=pk)
            instance.enabled = False
            instance.save()
            return Response().common
        except Exception as e:
            print(e)
            return Response(str(e)).internal_server_error