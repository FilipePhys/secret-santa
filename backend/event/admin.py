from django.contrib import admin

from .models import EventDay, Participant


class ParticipantAdmin(admin.TabularInline):
    model = Participant
    extra = 1


class EventDayAdmin(admin.ModelAdmin):
    inlines = (ParticipantAdmin, )
    model = EventDay
    list_display = ['id', 'event_name', 'author', 'date_time', 'location', ]
    fields = ['author', 'event_name', 'event_description', 'date_time', 'location', 'marmalade', ]


admin.site.register(EventDay, EventDayAdmin)
