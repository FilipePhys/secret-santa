from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'birth_date', 'is_staff', 'is_active', 'last_login', 'date_joined', ]
    #readonly_fields = ['friend', ]
    fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'profile_img', 'friend', ]#'groups', ]


admin.site.register(CustomUser, CustomUserAdmin)
