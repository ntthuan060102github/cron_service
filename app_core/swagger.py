from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="My PT - Cron Management Service",
      default_version="1.0.0",
      description="My PT - Cron Management Service",
      terms_of_service="",
      contact=openapi.Contact(name="Nguyen Trong Thuan", email="thuannt29@fpt.com.vn")
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urls = [
    # re_path(
    #     r'^swagger(?P<format>\.json|\.yaml)$', 
    #     schema_view.without_ui(cache_timeout=0), 
    #     name='schema-json'
    # ),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]