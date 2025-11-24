# python manage.py shell

import zoneinfo
from datetime import datetime, timedelta


def get_quarter_range_in_timezone(year, quarter, timezone_str):
    tz = zoneinfo.ZoneInfo(timezone_str)
    start_of_quarter = datetime(year, 3 * (quarter - 1) + 1, 1, 0, 0, 0, tzinfo=tz)
    start_of_next_quarter = (
        datetime(year, 3 * quarter + 1, 1, 0, 0, 0, tzinfo=tz)
        if quarter < 4
        else datetime(year + 1, 1, 1, 0, 0, 0, tzinfo=tz)
    )
    end_of_quarter = start_of_next_quarter - timedelta(microseconds=1)
    return start_of_quarter.isoformat(), end_of_quarter.isoformat()


get_quarter_range_in_timezone(2025, 1, "America/Los_Angeles")
# ('2025-01-01T00:00:00-08:00', '2025-03-31T23:59:59.999999-07:00')
get_quarter_range_in_timezone(2025, 1, "America/New_York")
# ('2025-01-01T00:00:00-05:00', '2025-03-31T23:59:59.999999-04:00')
get_quarter_range_in_timezone(2025, 1, "Europe/London")
# ('2025-01-01T00:00:00+00:00', '2025-03-31T23:59:59.999999+01:00')
get_quarter_range_in_timezone(2025, 1, "Europe/Rome")
# ('2025-01-01T00:00:00+01:00', '2025-03-31T23:59:59.999999+02:00')
get_quarter_range_in_timezone(2025, 1, "Asia/Tokyo")
# ('2025-01-01T00:00:00+09:00', '2025-03-31T23:59:59.999999+09:00')
get_quarter_range_in_timezone(2025, 1, "Australia/Sydney")
# ('2025-01-01T00:00:00+11:00', '2025-03-31T23:59:59.999999+11:00')

# Notice that the timezone offsets are different
# in a few timezones because of Daylight Saving Time changes in Q1.
