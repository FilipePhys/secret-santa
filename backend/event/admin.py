from django.contrib import admin

from .models import EventDay, Participant


class ParticipantAdmin(admin.TabularInline):
    model = Participant
    extra = 1
    fields = ['participant', 'drawn', ]
    readonly_fields = ['drawn', ]


class EventDayAdmin(admin.ModelAdmin):
    inlines = (ParticipantAdmin, )
    model = EventDay
    list_display = ['id', 'event_name', 'author', 'date_time', 'location', ]
    fields = ['author', 'event_name', 'event_description', 'date_time', 'location', 'marmalade', ]

    actions = ['draw']

    @admin.action(description='Make the draw')
    def draw(self, request, queryset):
        print("The draw Process Started")
        for event in queryset:
            event.save_draw_models()


admin.site.register(EventDay, EventDayAdmin)
