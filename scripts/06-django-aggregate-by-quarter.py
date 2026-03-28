# python manage.py shell

from django.db.models import Count
from django.db.models.functions import TruncQuarter
from timezone_test_app.models import TimezoneTest

# extract count of all 2025 records, grouping them by quarter

qs = (
    TimezoneTest.objects.filter(value_dt__year=2025)
    .annotate(quarter=TruncQuarter("value_dt"))
    .values("quarter")
    .annotate(count=Count("id"))
    .order_by("quarter")
)
for record in qs:
    year = record["quarter"].year
    quarter = (record["quarter"].month - 1) // 3 + 1
    records = record["count"]
    print(f"{year}-Q{quarter}: {records} record(s)")
