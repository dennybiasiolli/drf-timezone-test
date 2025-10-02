from django.db import models

class TimezoneTest(models.Model):
    value_str = models.CharField(max_length=50)
    value_dt = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value_str
