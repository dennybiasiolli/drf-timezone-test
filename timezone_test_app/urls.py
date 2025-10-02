from django.urls import include, path
from rest_framework import routers

from .views import TimezoneTestViewSet


router = routers.DefaultRouter()
router.register(r'timezone-tests', TimezoneTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
