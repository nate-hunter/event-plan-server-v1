from django.shortcuts import render

from rest_framework import status
from rest_framework import viewsets, generics
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

  def get_queryset(self):
    queryset = Event.objects.all()
    name_params = self.request.query_params.get('name')

    if name_params is not None:
      queryset = queryset.filter(name__icontains=name_params)

    return queryset
