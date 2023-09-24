from django_celery_beat.models import CrontabSchedule
from rest_framework import serializers

class CronTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrontabSchedule
        exclude = ("timezone", )

    def create(self, validated_data):
        instance, _ = self.Meta.model.get_or_create(**validated_data)
        return instance