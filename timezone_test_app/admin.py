from django.contrib import admin

from .models import TimezoneTest

@admin.register(TimezoneTest)
class TimezoneTestAdmin(admin.ModelAdmin):
    list_display = ('value_str', 'value_dt', 'comment', 'created_at', 'modified_at')
    ordering = ('value_dt',)
