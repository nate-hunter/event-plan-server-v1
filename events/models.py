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

  date = models.DateTimeField(blank=True, null=True)
  # time_start = models.DateTimeField(blank=True)
  # time_end = models.DateTimeField(blank=True)

  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)

  # est_num_guests = models.IntegerField(blank=True, null=True)
  num_guests = models.IntegerField(blank=True, null=True)
  budget = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
  # est_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
  # est_cost_per_guest = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
  cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
  cost_per_guest = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

  # is_pinned = models.BooleanField(default=False)


class GuestList(models.Model):
  name = models.CharField(max_length=155, blank=True)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.event})'


# class Guest(models.Model):
#   first_name = models.CharField(max_length=155, blank=True)
#   last_name = models.CharField(max_length=155, blank=True)

#   def __str__(self):
#     name = f'{self.last_name}, {self.first_name}'
#     return self.name