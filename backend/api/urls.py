from django.urls import path
from .views import CustomUserList, CustomUserDetail

urlpatterns = [
    path('<int:pk>', CustomUserDetail.as_view(), name='detail_create'),
    path('', CustomUserList.as_view(), name='list_create'),
    ]
