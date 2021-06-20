from rest_framework import serializers

from event.models import EventDay
from user.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'birth_date', 'profile_img', 'friend', )


class EventDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventDay
        fields = ('id', 'author', 'event_name', 'event_description', 'date_time', 'location', )

