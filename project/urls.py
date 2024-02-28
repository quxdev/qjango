from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from project import errors

admin.site.site_header = getattr(settings, "SITE_HEADER", "Qjango by Qux")
admin.site.site_title = getattr(settings, "SITE_TITLE", "Qjango")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("impersonate/", include("impersonate.urls")),
    path("", include("qux.auth.urls.appurls", namespace="qux_auth")),
    path("", TemplateView.as_view(template_name="_blank.html"), name="home"),
    path("cover/", TemplateView.as_view(template_name="cover.html"), name="cover"),
    path("google/", TemplateView.as_view(template_name="google.html"), name="google"),
    path("", include("apps.gizmo.urls.appurls"), name="gizmo"),
]

handler400 = "project.errors.error_badrequest"
handler403 = "project.errors.error_forbidden"
handler404 = "project.errors.error_notfound"
handler500 = "project.errors.error_servererror"

if settings.DEBUG:
    urlpatterns += [
        path("error/400", errors.error_badrequest),
        path("error/403", errors.error_forbidden),
        path("error/404", errors.error_notfound),
        path("error/500", errors.error_servererror),
    ]

if settings.DEBUG and ("debug_toolbar" in settings.INSTALLED_APPS):
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
