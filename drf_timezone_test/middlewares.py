import zoneinfo

from django.utils import timezone


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # read the timezone name from a custom header (API requests)
        tzname = request.headers.get("X-Timezone")
        if not tzname:
            # fallback to reading the timezone name from a cookie (browser requests)
            tzname = request.COOKIES.get("django_timezone")

        if tzname:
            try:
                timezone.activate(zoneinfo.ZoneInfo(tzname))
            except zoneinfo.ZoneInfoNotFoundError:
                timezone.deactivate()
        else:
            timezone.deactivate()
        return self.get_response(request)
