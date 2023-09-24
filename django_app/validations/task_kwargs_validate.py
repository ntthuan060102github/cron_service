from rest_framework import serializers

class TaskKwargsValidate(serializers.Serializer):
    METHOD_CHOICES = [
        ("GET", "GET"), 
        ("POST", "POST"),
        ("PUT", "PUT"), 
        ("PATCH", "PATCH"), 
        ("DELETE", "DELETE")
    ]

    url = serializers.URLField(allow_blank=False, allow_null=False)
    method = serializers.ChoiceField(choices=METHOD_CHOICES, allow_null=False, allow_blank=False)
    headers = serializers.DictField(allow_null=True, default=None)
    data = serializers.DictField(allow_null=True, default=None)
    params = serializers.DictField(allow_null=True, default=None)
    proxies = serializers.DictField(allow_null=True, default=None)


