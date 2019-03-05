"""
URL Configuration
"""
from django.conf.urls import url
from django.urls import include
from django.contrib import admin

urlpatterns = [
    # url(r"^", include(public_urls)),
    url(r"^admin/", admin.site.urls),
    # url(r"^api/v1/", include(api_v1_urls)),
]

