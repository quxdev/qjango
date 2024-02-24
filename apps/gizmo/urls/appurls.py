from django.urls import path
from ..views.appviews import ApplicationHomeView


urlpatterns = [
    path("", ApplicationHomeView.as_view(), name="home"),
]
