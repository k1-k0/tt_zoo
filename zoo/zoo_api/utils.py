from rest_framework import serializers
from django.utils import timezone, datetime_safe


def date_validator(value):
    if value > datetime_safe.date.today():
        raise serializers.ValidationError('Date may not be higher than today')

def date_time_validator(value):
    if value > timezone.now():
        raise serializers.ValidationError('Date may not be higher than now')
