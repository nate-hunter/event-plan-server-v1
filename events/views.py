from django.shortcuts import render

from rest_framework import status
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventSerializer


class EventsViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
  serializer_class = EventSerializer
  queryset = Event.objects.all()

  def get_queryset(self):
    queryset = Event.objects.all().order_by('name')
    name_params = self.request.query_params.get('name')

    if name_params is not None:
      queryset = queryset.filter(name__icontains=name_params)

    return queryset
