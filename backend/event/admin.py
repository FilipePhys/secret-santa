from django.contrib import admin

from .models import EventDay


class EventDayAdmin(admin.ModelAdmin):
    model = EventDay
    list_display = ['id', 'event_name', 'author', 'date_time', 'location', ]
    fields = ['author', 'event_name', 'event_description', 'date_time', 'location', ]#'participants', ]


admin.site.register(EventDay, EventDayAdmin)
