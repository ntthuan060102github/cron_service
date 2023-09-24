import uuid
import json
from rest_framework import serializers
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django_app.validations.task_kwargs_validate import TaskKwargsValidate
from django_app.serializers.cron_tab_serializer import CronTabSerializer

class PeriodicTaskSerializer(serializers.ModelSerializer):
    abs_task_path = "django_app.tasks.cron_tasks.abstract_request_api_task"
    
    def __init__(self, *args, **kwargs):
        existing = set(self.fields.keys())
        relation = bool(kwargs.pop("relation", True))
        allowed = kwargs.pop("fields", []) or existing
        excluded = kwargs.pop("excluded", [])
        
        super().__init__(*args, **kwargs)

    class Meta:
        model = PeriodicTask
        exclude = (
            "clocked", 
            "solar", 
            "interval", 
            "args", 
            "routing_key",
            "queue"
        )
        read_only_fields = (
            "id", 
            "last_run_at",
            "total_run_count", 
            "date_changed", 
            "enabled", 
            "task", 
            "name"
        )

    kwargs = TaskKwargsValidate(required=True, many=False)
    crontab = CronTabSerializer(required=True, many=False)

    def create(self, validated_data):
        cron_instance, _ = CrontabSchedule.objects.get_or_create(**validated_data["crontab"])
        validated_data["task"] = self.abs_task_path
        validated_data["name"] = uuid.uuid4().hex
        validated_data["crontab"] = cron_instance
        validated_data["kwargs"] = json.dumps(validated_data["kwargs"])
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if "kwargs" in validated_data:
            validated_data["kwargs"] = json.dumps(validated_data["kwargs"])
        return super().update(instance, validated_data)