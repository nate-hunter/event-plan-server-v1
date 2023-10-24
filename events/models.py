from django.db import models


class Event(models.Model):
  """Event model."""
  WEDDING = 'wedding'
  OTHER = 'other'
  EVENT_TYPES = [
    (WEDDING, 'Wedding'),
    (OTHER, 'other'),
  ]

  event_type = models.CharField(max_length=150, blank=True, choices=EVENT_TYPES)
  name = models.CharField(max_length=150, blank=True)
  description = models.TextField(blank=True)
  details = models.TextField(blank=True)

  date = models.DateTimeField(blank=True)
  # time_begin = models.DateTimeField(blank=True)
  # time_ennd = models.DateTimeField(blank=True)

  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)

  budget = models.DecimalField(max_digits=19, decimal_places=4, blank=True)

  num_guests = models.IntegerField(blank=True)
  cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True)
  cost_per_guest = models.DecimalField(max_digits=19, decimal_places=4, blank=True)

  is_pinned = models.BooleanField(default=False)
  # color = models.CharField(max_length=150, blank=True) # QUESTON: Make this a model? `Many-to-Many`?


