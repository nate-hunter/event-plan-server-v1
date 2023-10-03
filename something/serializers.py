from rest_framework import serializers

from something.models import Thing

class ThingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thing
    fields = ['id', 'name', 'description', 'created_at', 'updated_at']
    read_only_fields = ['id']