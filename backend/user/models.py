from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(upload_to='profile_img', null=True, blank=True)
    who_am_I = models.TextField(null=True, blank=True)
    relationship = models.ForeignKey(to='CustomUser', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='date', )

    def __str__(self):
        return self.username


class Friends(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True, blank=True,
                             related_name='owner_friends_group', )
    friend = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, null=True, blank=True,
                                  related_name='friends', )
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"friends since {self.added_date}"

    class Meta:
        unique_together = (('user', 'friend'), )
