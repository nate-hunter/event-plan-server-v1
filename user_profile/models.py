from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=155, blank=True)
  last_name = models.CharField(max_length=155, blank=True)
  phone_number_1 = models.CharField(max_length=20, blank=True)
  address_city = models.CharField(max_length=155, blank=True)

  def __str__(self):
      return f'{self.first_name} {self.last_name}'

