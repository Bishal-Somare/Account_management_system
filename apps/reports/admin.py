from django.contrib import admin

# Register your models here.
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['ReportID', 'AccountID', 'TransactionID', 'DateRange', 'Status']
    list_filter = ['Status', 'DateRange']
    search_fields = ['ReportID']
    date_hierarchy = 'DateRange'

