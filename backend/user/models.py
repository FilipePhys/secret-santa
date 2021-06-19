from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(upload_to='profile_img', null=True, blank=True)
    who_am_I = models.TextField(null=True, blank=True)
    friend = models.ManyToManyField(to='CustomUser', symmetrical=False, blank=True,
                                    related_name='friends',)
    relationship = models.ForeignKey(to='CustomUser', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='date', )

    def __str__(self):
        return self.username
