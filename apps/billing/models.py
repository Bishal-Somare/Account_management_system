from django.db import models
from apps.reports.models import Report
# Create your models here.

class Invoice(models.Model):
    IVID = models.CharField(max_length=50, primary_key=True)
    ReportID = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='invoices')
    BalanceDue = models.DecimalField(max_digits=15, decimal_places=2)
    POno = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    Description = models.TextField()
    UnitPrice = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.IVID}"