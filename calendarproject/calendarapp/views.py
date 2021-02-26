from django.shortcuts import render, get_object_or_404
from django.views import generic
from datetime import datetime, date, timedelta
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.urls import reverse

import calendar

from .models import Event
from .my_calendar import Calendar
from .form import EventForm


# Create your views here.
def get_date(request):
    if request:
        year, month = (int(x) for x in request.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def previous_month(date):
    first_day = date.replace(day=1)
    month_prev = first_day - timedelta(days=1)
    return 'month=' + str(month_prev.year) + '-' + str(month_prev.month)


def next_month(date):
    days = calendar.monthrange(date.year, date.month)[1]
    last_day = date.replace(day=days)
    month_next = last_day + timedelta(days=1)
    return 'month=' + str(month_next.year) + '-' + str(month_next.month)


def change_event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid() and 'submit' in request.POST:
        form.save()
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    elif request.POST and 'delete' in request.POST and event_id:
        Event.objects.filter(pk=event_id).delete()
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'calendarapp/event.html', {'form': form})


class ViewCalendar(generic.ListView):
    model = Event
    template_name = 'calendarapp/calendarapp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date_today = get_date(self.request.GET.get('month', None))
        calendar_instance = Calendar(date_today.year, date_today.month)
        html_calendar = calendar_instance.formatmonth(year=True)
        context['calendar'] = mark_safe(html_calendar)
        context['previous_month'] = previous_month(date_today)
        context['next_month'] = next_month(date_today)
        return context
