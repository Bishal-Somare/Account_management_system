from django.contrib import admin

# Register your models here.
from .models import BalanceSheet

@admin.register(BalanceSheet)
class BalanceSheetAdmin(admin.ModelAdmin):
    list_display = ['BSID', 'ReportID', 'TotalLiabilities', 'TotalAssets', 'TotalOwnersEquity']
    search_fields = ['BSID']