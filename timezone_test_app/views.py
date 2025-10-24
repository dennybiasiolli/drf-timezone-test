from django.db.models.functions import ExtractDay, ExtractQuarter, ExtractYear
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .models import TimezoneTest
from .serializers import TimezoneTestSerializer


class TimezoneTestViewSet(viewsets.ModelViewSet):
    queryset = TimezoneTest.objects.all()
    serializer_class = TimezoneTestSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        "value_dt": ["gte", "lte", "exact", "gt", "lt"],
    }
    ordering_fields = ["value_dt"]
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def group_by_year_and_quarter(self, request):
        qs = self.filter_queryset(self.get_queryset())
        # qs = qs.extra(select={'year': "EXTRACT(year FROM value_dt)", 'quarter': "EXTRACT(quarter FROM value_dt)"}).values('year', 'quarter').order_by('year', 'quarter').distinct()
        qs = (
            qs.annotate(
                year=ExtractYear("value_dt"), quarter=ExtractQuarter("value_dt")
            )
            .values("year", "quarter")
            .order_by("year", "quarter")
            .distinct()
        )
        data = []
        for item in qs:
            year = int(item["year"])
            quarter = int(item["quarter"])
            items = list(
                self.get_queryset()
                .filter(value_dt__year=year, value_dt__quarter=quarter)
                .order_by("value_dt")
                .values()
            )
            data.append(
                {"year": year, "quarter": quarter, "count": len(items), "items": items}
            )
        return Response(data)
