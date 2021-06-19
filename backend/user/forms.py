from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('birth_date',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'birth_date', 'profile_img',)


class CustomUserUpdateForm(forms.ModelForm):

    password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'birth_date', 'profile_img', )

