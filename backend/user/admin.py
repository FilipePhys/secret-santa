from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Friends


class FriendsAdmin(admin.TabularInline):
    model = Friends
    fk_name = 'user'
    extra = 1


class CustomUserAdmin(admin.ModelAdmin):
    inlines = (FriendsAdmin, )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'username', 'email', 'birth_date', 'is_staff', 'is_active', 'last_login', 'date_joined', ]
    #readonly_fields = ['friend', ]
    fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'relationship', 'who_am_I', 'profile_img', ]


admin.site.register(CustomUser, CustomUserAdmin)
