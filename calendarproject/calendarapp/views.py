from django.shortcuts import render
from django.views import generic
from datetime import datetime, date
from django.utils.safestring import mark_safe

from .models import Event
from .my_calendar import Calendar


# Create your views here.
def get_date(request):
    if request:
        year, month = (int(x) for x in request.split('-'))
        return date(year, month, day=1)
    return datetime.today()


class ViewCalendar(generic.ListView):
    model = Event
    template_name = 'calendarapp/calendarapp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_today = get_date(self.request.GET.get('day', None))
        calendar_instance = Calendar(date_today.year, date_today.month)
        html_calendar = calendar_instance.formatmonth(year=True)
        context['calendar'] = mark_safe(html_calendar)
        return context
