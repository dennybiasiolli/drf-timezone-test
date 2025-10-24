# How much do you know about datetimes and timezones?

A quick overview of how timezones work, with examples in Python, PostgreSQL, Django and django-rest-framework,
and how to (try to) handle them correctly.

## What is a timestamp?

A timestamp is a representation of a specific point in time.

In the technical world, a timestamp is independent of timezones and it's usually represented as the number of seconds (or milliseconds/microseconds) since a specific epoch (e.g., January 1, 1970, 00:00:00 UTC for Unix timestamps).


#### Representation of a timestamp

A timestamp is typically represented as a numeric value, which is the number of seconds (or milliseconds) since the epoch. This representation is independent of timezones.

Since it's not easy for humans to read and understand, timestamps are often converted to human-readable date and time formats when displayed.

One common format for representing date and time with timezone information is the ISO 8601 format.

The ISO 8601 standard defines a textual representation of date and time, which can include timezone information.

https://en.wikipedia.org/wiki/ISO_8601

For example, `2025-10-05T14:48:00Z` represents October 5, 2025, at 14:48 UTC (the "Z" indicates UTC timezone), while `2025-10-05T10:48:00-04:00` represents the same moment in time in New York (Eastern Daylight Time).



## Timestamp representation in programming languages

#### JavaScript

A JavaScript date is fundamentally specified as the time in milliseconds
that has elapsed since the epoch (midnight January 1, 1970 UTC).

```js
const now = new Date();
console.log(now.getTime());
```

#### Python (time module)

A timestamp is represented as a floating point number,
where the integer portion represents the number of seconds
that have elapsed since the epoch (midnight January 1, 1970 UTC).

The decimal portion represents fractions of a second,
the precision depends on the platform.

```py
import time

now_timestamp = time.time()
print(now_timestamp)
```

#### Python (datetime module)

A simpler way to get the current timestamp in Python is to use the `datetime` module.
The range of representable values though is "only" from year 1 to 9999.

```py
from datetime import datetime

now = datetime.now()
print(now.timestamp())
```

It's important to note that while a timestamp itself does not contain timezone information,
it can be associated with a specific timezone when it is displayed or interpreted.


#### Python datetime with timezone

In Python, a `datetime` object can be
- "naive" (without timezone information)
- "aware" (with timezone information)

```py
import time
import zoneinfo
from datetime import datetime, timezone

# naive datetime (no timezone info, using the local timezone of the system)
naive_dt = datetime.now()
print(f"Naive datetime, using the local timezone of the system\n\t{repr(naive_dt)}")

# aware datetime (with timezone info)
aware_dt_utc = datetime.now(timezone.utc)
print(f"Aware datetime (UTC)\n\t{repr(aware_dt_utc)}")

# aware datetime with specific timezone name using zoneinfo (e.g., CET, or Europe/Rome)
local_tz_str = "CET" # Central European Time (standard time)
local_tz = zoneinfo.ZoneInfo(local_tz_str)
aware_dt_local_tz = datetime.now(local_tz)
print(f"Aware datetime (CET)\n\t{repr(aware_dt_local_tz)}")

# for a list of available timezones in zoneinfo
zoneinfo.available_timezones() # returns a set of all available timezone names


# check the difference between the timestamps
print(f"Difference between aware datetime ({local_tz_str}) and aware datetime (UTC) in `timedelta`:")
print(f"\t{repr(aware_dt_local_tz - aware_dt_utc)}")
```

While in Python it's tricky to get the local timezone name of the system,
you can use the `tzlocal` library to get the correct timezone name.

```py
import tzlocal

tzlocal.get_localzone()
```

In JavaScript, you can get the local timezone name of the browser with:

```js
Intl.DateTimeFormat().resolvedOptions().timeZone;
```


## PostgreSQL timestamptz

In PostgreSQL you can handle timestamps with timezone with the `timestamp with time zone` (aka `timestamptz`) type.

It's a common misconception that `timestamptz` stores the timezone information.
It doesn't. It stores the timestamp in UTC and converts it to the local timezone of the database
when you query it, or the timezone you set for the current session.

The storage size is 8 bytes, the same as the `timestamp without time zone` (aka `timestamp`) type.
They have a range from 4713 BC to 294276 AD with 1 microsecond resolution.

> https://www.postgresql.org/docs/current/datatype-datetime.html

---


Let's create a sample table to play with timezones:

[source](./scripts/01-create-sql-table.sql)


Let's say we have people in New York, Rome, Calcutta and Tokyo, and everyone wants to store
the start and end of Q1 2025 in their local timezone.

In a browser, using JavaScript and the `luxon` library, we can get the correct ISO string with timezone offset for each city like this:

[source](./scripts/02-get-js-date-ranges.js)

Notice that the timezone offsets are different because of Daylight Saving Time (DST), but all of this is handled automatically.


Now we can insert the values in the database:

[source](./scripts/03-insert-db-values.sql)


If we query the table, PostgreSQL will convert the `timestamptz` value to the local timezone of the database (Europe/Rome in my case).

```sql
select * from test_timezone order by value_dt;
```

You may notice that the `value_dt` column values are different from the `value_str` column values,
because PostgreSQL converted the timestamps to the local timezone of the database (Europe/Rome).


#### Querying ranges of dates with timestamptz

You might want to query the records between the start and end of Q1 2025.

```sql
-- Note: in postgres, `between` is inclusive of both ends

select * from test_timezone where value_dt >= '2025-01-01' and value_dt < '2025-04-01' order by value_dt;
-- or
select * from test_timezone where value_dt >= '2025-01-01 00:00:00' and value_dt < '2025-04-01 00:00:00' order by value_dt;
```

You need to be careful when querying ranges of dates, because the results will depend on the timezone of the database.
If you don't specify the timezone, PostgreSQL will use the database's timezone to interpret the dates.

In this case, this is correct if you want to get the records between the start and end of Q1 2025 in Europe/Rome timezone, because this is the default timezone of my local PostgreSQL database.

But what if you are connecting from New York and you want to get the records between the start and end of Q1 2025 in New York timezone?

You could specify the timezone offset in the query:


```sql
-- select dates between start and end of Q1 2025 in New York
select * from test_timezone where value_dt between '2025-01-01T00:00:00.000-05:00' and '2025-03-31T23:59:59.999-04:00' order by value_dt;
```

#### Checking the current timezone

You can check the current timezone with:

```sql
show timezone;
  TimeZone
-------------
 Europe/Rome
(1 row)
```

---

Where is the timezone of the database configured?

1. For the entire PostgreSQL server, in the `postgresql.conf` file with `timezone = 'Europe/Rome'`
2. In the connection string with `?options=-c%20TimeZone=Europe/Rome`
3. For a specific database, with `ALTER DATABASE db_name SET TIMEZONE TO 'Europe/Rome';`
4. For a specific user, with `ALTER ROLE user_name SET TIMEZONE TO 'Europe/Rome';`
5. For a single session, with `SET TIMEZONE TO 'Europe/Rome';`
6. For a single transaction, with `SET LOCAL TIMEZONE TO 'Europe/Rome';` within a transaction block


For example, if you want to get the records between the start and end of Q1 2025 in New York timezone, you can set the timezone for the transaction like this:

```sql
begin transaction;
SET LOCAL TIMEZONE TO 'America/New_York';
select * from test_timezone where value_dt >= '2025-01-01' and value_dt < '2025-04-01' order by value_dt;
end;

begin transaction;
SET LOCAL TIMEZONE TO 'Asia/Calcutta';
select * from test_timezone where value_dt >= '2025-01-01' and value_dt < '2025-04-01' order by value_dt;
end;
```

This way you can get results in your desired timezone without changing the database's timezone permanently.


## Django DateTimeField

In Django you can use the `DateTimeField` to store timestamps with timezone.
They will be stored in the database as `timestamptz` if you are using PostgreSQL.

If you don't specify a timezone when creating a `DateTimeField` object,
Django will assume the datetime is in the timezone specified in the `TIME_ZONE` setting (UTC by default).

Note that to enable timezone support in Django, you need to set `USE_TZ = True` in your settings (it's `True` by default).

Django will store all datetimes in UTC in the database and will use timezone-aware datetimes throughout the application.


What does this means for users in different timezones?
When a user in New York creates a datetime object without timezone information (a naive datetime), Django will assume that the datetime is in the timezone specified in `TIME_ZONE` (UTC by default) and will convert it to UTC before storing it in the database.

When a user in Rome creates a naive datetime, Django will do the same thing: assume it's in UTC and convert it to UTC before storing it.

When you query the database, Django will convert the UTC datetime back to the timezone specified in `TIME_ZONE` (UTC by default) before returning it to the application.

Let's try with an example, similar to the one we created for PostgreSQL.

[source](./timezone_test_app/models.py)

[source](./scripts/04-django-bulk-create.py)

```sql
select * from timezone_test_app_timezonetest order by value_dt;
 id |           value_str           |          value_dt          |          comment
----+-------------------------------+----------------------------+---------------------------
  5 | 2025-01-01T00:00:00.000+09:00 | 2024-12-31 16:00:00+01     | start of Q1 2025 in Tokyo
  3 | 2025-01-01T00:00:00.000+01:00 | 2025-01-01 00:00:00+01     | start of Q1 2025 in Rome
  1 | 2025-01-01T00:00:00.000-05:00 | 2025-01-01 06:00:00+01     | start of Q1 2025 in NY
  6 | 2025-03-31T23:59:59.999+09:00 | 2025-03-31 16:59:59.999+02 | end of Q1 2025 in Tokyo
  4 | 2025-03-31T23:59:59.999+02:00 | 2025-03-31 23:59:59.999+02 | end of Q1 2025 in Rome
  2 | 2025-03-31T23:59:59.999-04:00 | 2025-04-01 05:59:59.999+02 | end of Q1 2025 in NY
(6 rows)
```

```py
# python manage.py shell

from timezone_test_app.models import TimezoneTest

TimezoneTest.objects.filter(value_dt__gte="2025-01-01", value_dt__lt="2025-04-01").order_by("value_dt")
# RuntimeWarning: DateTimeField TimezoneTest.value_dt received a naive datetime (2025-01-01 00:00:00) while time zone support is active.
# RuntimeWarning: DateTimeField TimezoneTest.value_dt received a naive datetime (2025-04-01 00:00:00) while time zone support is active.
# <QuerySet [<TimezoneTest: start of Q1 2025 in NY>, <TimezoneTest: end of Q1 2025 in Tokyo>, <TimezoneTest: end of Q1 2025 in Rome>]>
```

This converts the naive datetimes to the timezone in settings.TIME_ZONE (UTC by default)

```py
TimezoneTest.objects.filter(value_dt__gte="2025-01-01T00:00:00.000-05:00", value_dt__lte="2025-03-31T23:59:59.999-04:00").order_by("value_dt")
# <QuerySet [<TimezoneTest: start of Q1 2025 in NY>, <TimezoneTest: end of Q1 2025 in Tokyo>, <TimezoneTest: end of Q1 2025 in Rome>, <TimezoneTest: end of Q1 2025 in NY>]>
```

## django-rest-framework DateTimeField

```py
from rest_framework import serializers, viewsets

class TimezoneTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimezoneTest
        fields = ["id", "value_str", "value_dt", "comment"]

class TimezoneTestViewSet(viewsets.ModelViewSet):
    queryset = TimezoneTest.objects.all()
    serializer_class = TimezoneTestSerializer
```

Example API requests to create records:

[source](./scripts/05-drf-POST-calls.sh)

```bash
# gets all records using the default timezone in settings.TIME_ZONE (UTC by default)\
curl -X GET "http://localhost:8001/api/timezone-tests/?value_dt__gte=2025-01-01&value_dt__lte=2025-04-01&ordering=value_dt"
```


## Custom HTTP Header

Create a Django middleware to read the header and set the timezone for the request.
The timezone will also be used for database queries.

[source](./drf_timezone_test/middlewares.py)

Add the middleware to the list of middlewares, BEFORE everything that needs to use the specific timezone to query the database.

```py
MIDDLEWARE = [
    # ...
    'drf_timezone_test.middlewares.TimezoneMiddleware'
]
```


Get the local timezone of the browser with JavaScript

```js
Intl.DateTimeFormat().resolvedOptions().timeZone;
```

Send the value to the backend with a custom HTTP header

```bash
curl -X GET "http://localhost:8001/api/timezone-tests/?ordering=value_dt" \
    -H "Content-Type: application/json" \
    -H "X-Timezone: Europe/Rome"
```


```bash
curl -X GET http://localhost:8001/api/timezone-tests/?value_dt__gte=2025-01-01&value_dt__lte=2025-04-01&ordering=value_dt \
    -H "X-Timezone: America/New_York"

# or specify the timezone offset directly

curl -X GET http://localhost:8001/api/timezone-tests/?value_dt__gte=2025-01-01T00:00:00.000-05:00&value_dt__lte=2025-03-31T23:59:59.999-04:00&ordering=value_dt
```


## Group By queries

```bash
curl -X GET http://localhost:8001/api/timezone-tests/group_by_year_and_quarter/ \
    -H "X-Timezone: America/New_York"

curl -X GET http://localhost:8001/api/timezone-tests/group_by_year_and_quarter/ \
    -H "X-Timezone: Europe/Rome"

curl -X GET http://localhost:8001/api/timezone-tests/group_by_year_and_quarter/ \
    -H "X-Timezone: Asia/Tokyo"

```
