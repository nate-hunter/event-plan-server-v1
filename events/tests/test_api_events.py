from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from events.models import Event
from events.tests import factories

class EventAPITests(TestCase):
  """Tests for Event API request"""

  def setUp(self):
    self.client = APIClient()

  def test_retrieve_events(self):

    e1 = factories.EventFactory.create()
    e2 = factories.EventFactory.create()
    e3 = factories.EventFactory.create()

    response = self.client.get(reverse('events-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 3)
    # import pdb; pdb.set_trace()
