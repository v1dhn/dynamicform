from django.db import models
from django.contrib.auth.models import User
import json

class Profile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    # Store dynamic fields data in JSON format
    additional_data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class DynamicField(models.Model):
    FIELD_TYPES = (
        ('char', 'CharField'),
        ('int', 'IntegerField'),
    )

    name = models.CharField(max_length=50, unique=True)
    field_type = models.CharField(max_length=10, choices=FIELD_TYPES)
    max_length = models.IntegerField(null=True, blank=True)  # Only for CharFields

    def __str__(self):
        return self.name
