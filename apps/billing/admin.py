from django.contrib import admin

# Register your models here.
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['IVID', 'ReportID', 'BalanceDue', 'POno', 'Quantity', 'UnitPrice']
    search_fields = ['IVID', 'POno']
    list_filter = ['BalanceDue']