from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        super(Calendar, self).__init__()
        self.year = year
        self.month = month

    def formatday(self, day, events):
        this_day_events = events.filter(start_time__day=day)
        html_day = ''
        for event in this_day_events:
            html_day += f'<li> {event.title} </li>'

        if day == 0:
            return '<td></td>'
        return f'<td><span class=\'date\'>{day}</span><ul> {html_day} </ul></td>'

    def formatweek(self, week, events):
        html_week = ''
        for day, weekday in week:
            html_week += self.formatday(day, events)
        return f'<tr> {html_week} </tr>'

    def formatmonth(self, year=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        html_month = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n' \
                     f'{self.formatmonthname(self.year, self.month, withyear=year)}\n' \
                     f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            html_month += f'{self.formatweek(week, events)}'
        return html_month
