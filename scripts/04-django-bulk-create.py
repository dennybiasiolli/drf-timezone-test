# python manage.py shell

from timezone_test_app.models import TimezoneTest


TimezoneTest.objects.bulk_create([
    TimezoneTest(
        value_str="2025-01-01T00:00:00.000-05:00",
        value_dt="2025-01-01T00:00:00.000-05:00",
        comment="start of Q1 2025 in NY"
    ),
    TimezoneTest(
        value_str="2025-03-31T23:59:59.999-04:00",
        value_dt="2025-03-31T23:59:59.999-04:00",
        comment="end of Q1 2025 in NY"
    ),
    TimezoneTest(
        value_str="2025-01-01T00:00:00.000+01:00",
        value_dt="2025-01-01T00:00:00.000+01:00",
        comment="start of Q1 2025 in Rome"
    ),
    TimezoneTest(
        value_str="2025-03-31T23:59:59.999+02:00",
        value_dt="2025-03-31T23:59:59.999+02:00",
        comment="end of Q1 2025 in Rome"
    ),
    TimezoneTest(
        value_str="2025-01-01T00:00:00.000+09:00",
        value_dt="2025-01-01T00:00:00.000+09:00",
        comment="start of Q1 2025 in Tokyo"
    ),
    TimezoneTest(
        value_str="2025-03-31T23:59:59.999+09:00",
        value_dt="2025-03-31T23:59:59.999+09:00",
        comment="end of Q1 2025 in Tokyo"
    ),
])
