from datetime import datetime, timedelta
import factory
import pytz
import random

from django.utils import timezone

from events.models import Event

from django.conf import settings
from django.utils.timezone import make_aware


def _create_date(days):
  date = datetime.now() + timedelta(days=days)
  return datetime(date.year, date.month, date.day, tzinfo=pytz.UTC)

def _get_num_guests(beg, end):
  return random.randint(beg, end)

def _get_cost_per_guest(budget, guest):
  return budget / guest

class EventFactory(factory.django.DjangoModelFactory):

  class Meta:
    model = Event

  name = factory.Sequence(lambda n: (f'TEST EVENT {n + 1}'))
  event_type = Event.EVENT_TYPES[0][0]

  # description = factory.Faker(
  #   'sentence',
  #   nb_words=8,
  # )
  description = factory.Faker('catch_phrase')

  date = factory.Faker(
    'date_between_dates',
    date_start=_create_date(1),
    date_end=_create_date(365*2),
  )

  # num_guests = factory.Faker('pyint', min_value=20, max_value=500)
  num_guests = factory.LazyAttribute(lambda x: _get_num_guests(20, 500))
  budget = factory.Faker('pyint', min_value=1000, max_value=100000)
  cost_per_guest = factory.LazyAttribute(
    lambda e: round(e.budget / e.num_guests, 2)
  )
  cost = factory.LazyAttribute(
    lambda e: e.budget * 0.2 + e.budget
  )