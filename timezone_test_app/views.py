from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import TimezoneTest
from .serializers import TimezoneTestSerializer


class TimezoneTestViewSet(viewsets.ModelViewSet):
    queryset = TimezoneTest.objects.all()
    serializer_class = TimezoneTestSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'value_dt': ['gte', 'lte', 'exact', 'gt', 'lt'],
    }
    ordering = ['value_dt']
    # permission_classes = [permissions.IsAuthenticated]
