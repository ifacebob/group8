from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('middle_name', 'gender', 'date_of_birth')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)