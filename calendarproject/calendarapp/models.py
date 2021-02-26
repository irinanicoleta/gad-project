from django.db import models
from django.urls import reverse


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    location = models.CharField(max_length=255, default=None)
    details = models.TextField()

    @property
    def get_url_html(self):
        url = reverse('calendarapp:edit_event', args=(self.id,))
        return f'<a href="{url}"> {self.name} </a>'
