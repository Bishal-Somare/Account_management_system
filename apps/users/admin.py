from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import AmsUser

@admin.register(AmsUser)
class AmsUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'Permissions', 'Status']
    list_filter = ['Permissions', 'Status', 'is_staff', 'is_active']
    search_fields = ['username', 'first_name', 'last_name', 'email', ]
    
    # Add custom fields to the form
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ( 'Permissions', 'Status')}),
    )