from django.db import models
from user.models import CustomUser


class EventDay(models.Model):
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE,
                               related_name='creator', null=True, blank=True, )
    event_name = models.CharField(max_length=47)
    event_description = models.CharField(max_length=250)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=150)
    marmalade = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(EventDay, self).save(*args, **kwargs)
            participant = Participant(event=self, participant=self.author)
            participant.save()
        else:
            super(EventDay, self).save(*args, **kwargs)


class Participant(models.Model):
    event = models.ForeignKey(to=EventDay, on_delete=models.CASCADE, related_name='event_day')
    participant = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,
                                    related_name='participant_in_event', )
    drawn = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,
                              default=None, related_name='participant_drawn', )

    class Meta:
        unique_together = (('event', 'participant'),
                           ('event', 'drawn'), )

    def __str__(self):
        return f"{self.participant} going to {self.event}"


