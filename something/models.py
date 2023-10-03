from django.db import models

class Thing(models.Model):
  """Test model for testing DRF deployement."""

  name =  models.CharField(max_length=155)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.name
