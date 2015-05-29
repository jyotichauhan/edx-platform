"""
URLs for the credit app.
"""
from django.conf import settings
from django.conf.urls import patterns, url

from .views import create_credit_request, credit_provider_callback

urlpatterns = []

if settings.FEATURES.get("ENABLE_CREDIT_API"):
    urlpatterns += patterns(
        '',

        url(
            r"^v1/provider/(?P<provider_id>[^/]+)/request/$",
            create_credit_request,
            name="credit_create_request"
        ),

        url(
            r"^v1/provider/(?P<provider_id>[^/]+)/callback/?$",
            credit_provider_callback,
            name="credit_provider_callback"
        ),
    )
