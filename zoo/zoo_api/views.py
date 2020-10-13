from rest_framework import viewsets
from rest_framework import permissions
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


class ZookeeperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows zookeeper to be viewed or edited.
    """
    queryset = Zookeeper.objects.all().order_by('-created_at')
    serializer_class = ZookeeperSerializer
    permission_classes = [permissions.IsAuthenticated]