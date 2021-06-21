from rest_framework import generics
from user.models import CustomUser
from event.models import EventDay


from .serializers import CustomUserSerializer, EventDaySerializer


class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class EventDayList(generics.ListCreateAPIView):
    queryset = EventDay.objects.all()
    serializer_class = EventDaySerializer


class EventDayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventDay.objects.all()
    serializer_class = EventDaySerializer
