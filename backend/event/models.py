from django.db import models
from user.models import CustomUser


class EventDay(models.Model):
    author = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='creator',
                               default='CustomUser_here', )
    event_name = models.CharField(max_length=47)
    event_description = models.CharField(max_length=250)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=150)

    #participants = models.ManyToManyField(to=CustomUser, blank=True, related_name='people', )

    def __str__(self):
        return self.event_name
