from django.db import models
from user.models import CustomUser


class EventDay(models.Model):
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='creator',
                               default='custom_user_here', )
    event_name = models.CharField(max_length=47)
    event_description = models.CharField(max_length=250)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=150)



    def __str__(self):
        return self.event_name


class Participant(models.Model):
    event = models.ForeignKey(to=EventDay, on_delete=models.CASCADE, related_name='event_day')
    participant = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,
                                    related_name='participant_in_event',)
    drawn = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,
                              default=models.SET_NULL, related_name='participant_drawn', )
