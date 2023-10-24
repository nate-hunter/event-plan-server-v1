from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id', 'event_type', 'name', 'description', 'details', 'date', 'created_at', 'updated_at', 'budget',]
    read_only_fields = ['id',]