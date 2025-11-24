# python manage.py shell

from timezone_test_app.models import TimezoneTest


TimezoneTest.objects.bulk_create(
    [
        TimezoneTest(
            value_str="2025-01-01T00:00:00-08:00",
            value_dt="2025-01-01T00:00:00-08:00",
            comment="start of Q1 2025 in LA",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999-07:00",
            value_dt="2025-03-31T23:59:59.999999-07:00",
            comment="end of Q1 2025 in LA",
        ),
        TimezoneTest(
            value_str="2025-01-01T00:00:00-05:00",
            value_dt="2025-01-01T00:00:00-05:00",
            comment="start of Q1 2025 in NY",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999-04:00",
            value_dt="2025-03-31T23:59:59.999999-04:00",
            comment="end of Q1 2025 in NY",
        ),
        TimezoneTest(
            value_str="2025-01-01T00:00:00+00:00",
            value_dt="2025-01-01T00:00:00+00:00",
            comment="start of Q1 2025 in London",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999+01:00",
            value_dt="2025-03-31T23:59:59.999999+01:00",
            comment="end of Q1 2025 in London",
        ),
        TimezoneTest(
            value_str="2025-01-01T00:00:00+01:00",
            value_dt="2025-01-01T00:00:00+01:00",
            comment="start of Q1 2025 in Rome",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999+02:00",
            value_dt="2025-03-31T23:59:59.999999+02:00",
            comment="end of Q1 2025 in Rome",
        ),
        TimezoneTest(
            value_str="2025-01-01T00:00:00+09:00",
            value_dt="2025-01-01T00:00:00+09:00",
            comment="start of Q1 2025 in Tokyo",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999+09:00",
            value_dt="2025-03-31T23:59:59.999999+09:00",
            comment="end of Q1 2025 in Tokyo",
        ),
        TimezoneTest(
            value_str="2025-01-01T00:00:00+11:00",
            value_dt="2025-01-01T00:00:00+11:00",
            comment="start of Q1 2025 in Sydney",
        ),
        TimezoneTest(
            value_str="2025-03-31T23:59:59.999999+11:00",
            value_dt="2025-03-31T23:59:59.999999+11:00",
            comment="end of Q1 2025 in Sydney",
        ),
    ]
)
