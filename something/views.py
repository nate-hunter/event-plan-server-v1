from django.shortcuts import render

from rest_framework import viewsets

from something import serializers
from something.models import Thing


class ThingViewSet(viewsets.ModelViewSet):
  queryset = Thing.objects.all()
  serializer_class = serializers.ThingSerializer
