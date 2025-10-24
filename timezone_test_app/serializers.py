from rest_framework import serializers

from .models import TimezoneTest


class TimezoneTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimezoneTest
        fields = ["id", "value_str", "value_dt", "comment", "created_at", "modified_at"]
