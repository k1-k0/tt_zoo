from rest_framework import serializers
from .models import (
    Animal, AnimalType, Room, Zookeeper
)

from . import utils


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

    birth_date = serializers.DateField(validators=[utils.date_validator])
    created_at = serializers.DateTimeField(validators=[utils.date_time_validator])
    updated_at = serializers.DateTimeField(validators=[utils.date_time_validator])


class AnimalTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'

    created_at = serializers.DateTimeField(validators=[utils.date_time_validator])
    updated_at = serializers.DateTimeField(validators=[utils.date_time_validator])


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    created_at = serializers.DateTimeField(validators=[utils.date_time_validator])
    updated_at = serializers.DateTimeField(validators=[utils.date_time_validator])


class ZookeeperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zookeeper
        fields = '__all__'

    birth_date = serializers.DateField(validators=[utils.date_validator])
    hire_date = serializers.DateTimeField(validators=[utils.date_validator])
    created_at = serializers.DateTimeField(validators=[utils.date_time_validator])
    updated_at = serializers.DateTimeField(validators=[utils.date_time_validator])