from django.shortcuts import render

from rest_framework import viewsets

from events.models import Event
from events.serializers import EventSerializer

class EventsViewSet(viewsets.ModelViewSet):
  serializer_class = EventSerializer
  queryset = Event.objects.all()