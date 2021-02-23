from django.conf.urls import url
from . import views

app_name = 'calendarapp'
urlpatterns = [
    url(r'^calendar/$', views.ViewCalendar.as_view(), name='calendar'),
]