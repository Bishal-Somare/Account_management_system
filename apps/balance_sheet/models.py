from django.db import models
from apps.reports.models import Report

class BalanceSheet(models.Model):
    BSID = models.CharField(max_length=50, primary_key=True)
    ReportID = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='balance_sheets')
    TotalLiabilities = models.DecimalField(max_digits=15, decimal_places=2)
    TotalAssets = models.DecimalField(max_digits=15, decimal_places=2)
    TotalOwnersEquity = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Balance Sheet {self.BSID}"