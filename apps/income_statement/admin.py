from django.contrib import admin

# Register your models here.
from .models import IncomeStatement

@admin.register(IncomeStatement)
class IncomeStatementAdmin(admin.ModelAdmin):
    list_display = ['ISID', 'ReportID', 'TotalRevenue', 'TotalExpense', 'NetIncome']
    search_fields = ['ISID']