from rest_framework import viewsets
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from zoo.zoo_api.serializers import (
    AnimalSerializer, AnimalTypeSerializer, RoomSerializer, ZookeeperSerializer
)
from .models import (
    Animal, AnimalType, Room, Zookeeper
)


class AnimalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals to be viewed or edited.
    """
    queryset = Animal.objects.all().order_by('-created_at')
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = {
        'birth_date': ['exact', 'gte', 'lte'],
        'last_seen': ['exact', 'gte', 'lte'],
        'gender': ['exact'],
        'family': ['exact'],
        'keeper': ['exact'],
        'room': ['exact']
    }


class AnimalTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows animals type to be viewed or edited.
    """
    queryset = AnimalType.objects.all().order_by('-created_at')
    serializer_class = AnimalTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows room to be viewed or edited.
    """
    queryset = Room.objects.all().order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'area': ['exact', 'gte', 'lte'],
        'room_type': ['exact']
    }


class ZookeeperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows zookeeper to be viewed or edited.
    """
    queryset = Zookeeper.objects.all().order_by('-created_at')
    serializer_class = ZookeeperSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = {
        'birth_day': ['exact', 'gte', 'lte'],
        'hire_date': ['exact', 'gte', 'lte'],
        'gender': ['exact'],
        'salary': ['exact', 'gte', 'lte'],
        'room': ['exact']
    }