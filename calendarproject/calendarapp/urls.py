from django.conf.urls import url
from . import views

app_name = 'calendarapp'
urlpatterns = [
    # url pentru calendar (pagina principala)
    url(r'^calendar/$', views.ViewCalendar.as_view(), name='calendar'),
    # url pentru un nou eveniment
    url(r'^event/new/$', views.change_event, name='new_event'),
    # url pentru editarea unui eveniment existent
    url(r'^event/(?P<event_id>\d+)/$', views.change_event, name='edit_event'),
]