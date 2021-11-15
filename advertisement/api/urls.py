from django.urls import path, include
from rest_framework import routers

from advertisement.api import views

app_name = "advertisement_api"

router = routers.DefaultRouter()
router.register(r"app_performances", views.AppPerformanceViewSet, basename='app_performance')

urlpatterns = [
    path("", include(router.urls)),
]
