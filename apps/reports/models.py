from django.db import models
from apps.users.models import AmsUser
from apps.transactions.models import Transaction

class Report(models.Model):
    ReportID = models.AutoField(primary_key=True)
    AccountID = models.ForeignKey(AmsUser, on_delete=models.CASCADE, related_name='reports')
    TransactionID = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='reports')
    DateRange = models.DateField()
    Status = models.CharField(max_length=50, default='draft')

    def __str__(self):
        return f"Report {self.ReportID}"


