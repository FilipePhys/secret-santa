from django.urls import path
from .views import CustomUserList, CustomUserDetail, EventDayDetail, EventDayList

urlpatterns = [
    path('event/<int:pk>', EventDayDetail.as_view(), name='detail_create_event'),
    path('event/', EventDayList.as_view(), name='list_create_event'),
    path('user/<int:pk>', CustomUserDetail.as_view(), name='detail_create_user'),
    path('user/', CustomUserList.as_view(), name='list_create_user'),
    ]
