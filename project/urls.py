from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView

admin.site.site_header = getattr(settings, "SITE_HEADER", "Qjango by Qux")
admin.site.site_title = getattr(settings, "SITE_TITLE", "Qjango")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("impersonate/", include("impersonate.urls")),
    path("", include("qux.auth.urls.appurls", namespace="qux_auth")),
    path("", TemplateView.as_view(template_name="qjango.html"), name="home"),
    path("", include("apps.gizmo.urls.appurls"), name="gizmo"),
]

if settings.DEBUG and ('debug_toolbar' in settings.INSTALLED_APPS):
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
