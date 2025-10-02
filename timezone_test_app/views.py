from rest_framework import permissions, viewsets

from .models import TimezoneTest
from .serializers import TimezoneTestSerializer


class TimezoneTestViewSet(viewsets.ModelViewSet):
    queryset = TimezoneTest.objects.all()
    serializer_class = TimezoneTestSerializer
    permission_classes = [permissions.IsAuthenticated]
