from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('national_code', 'full_name', 'phone', 'is_admin')
    list_filter = ('is_admin', )

    fieldsets = (
        (None, {'fields': ('national_code', 'full_name', 'phone', 'email', 'photo', 'sex', 'password')}),
        ('permission', {'fields': ('is_admin', 'is_active', 'directorship', 'is_inspector', 'last_login')}),
    )
    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('national_code', 'full_name', 'phone', 'email', 'photo', 'sex', 'password'),
    }),
    )

    ordering = ('join_date', )
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
