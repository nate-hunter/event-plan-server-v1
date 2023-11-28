from django.test import TestCase
from django.forms.models import model_to_dict

from events.models import Event

class EventModelTestCase(TestCase):
  """Tests for the Event model"""

  def test_create_event(self):
    """Test that creating an Event is successfull"""

    data = {
      'name': 'H.A. Wedding',
      'event_type': Event.EVENT_TYPES[0][0], # 'wedding'
      'description': 'Nate + Lisa wedding on Oahu',
      'details': 'A celebration of life, love, and culture through magic, nature, music, food, and drinks',
      'budget': 999999,
      'num_guests': 400,
      'cost_per_guest': 1000,
    }


    event = Event.objects.create(
      name=data['name'],
      event_type=data['event_type'],
      description=data['description'],
      details=data['details'],
      budget=data['budget'],
      num_guests=data['num_guests'],
      cost_per_guest=data['cost_per_guest']
    )

    self.assertEqual(event.name, data['name'])
    self.assertEqual(event.event_type, data['event_type'])