from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    details = models.TextField()
