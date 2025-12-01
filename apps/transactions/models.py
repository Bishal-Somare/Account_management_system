from django.db import models
from apps.users.models import AmsUser

class Transaction(models.Model):
    TransactionID = models.AutoField(primary_key=True)
    AccountID = models.ForeignKey(AmsUser, on_delete=models.CASCADE, related_name='transactions')
    DateOfTransaction = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(blank=True)
    BankName = models.CharField(max_length=100)
    Debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    Credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    TotalAmount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Transaction {self.TransactionID}"

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    TransactionID = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='payments')
    Currency = models.CharField(max_length=10, default='USD')
    Amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Payment {self.PaymentID}"


class CreditCard(models.Model):
    CreditCardNo = models.CharField(max_length=20, primary_key=True)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='credit_card')
    BankCredit = models.CharField(max_length=100)
    NameCredit = models.CharField(max_length=100)

    def __str__(self):
        return f"Card {self.CreditCardNo}"


class Cash(models.Model):
    CashTransactionNo = models.CharField(max_length=50, primary_key=True)
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='cash')
    NameCash = models.CharField(max_length=100)
    CashTendered = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Cash {self.CashTransactionNo}"


# class Cheque(models.Model):
#     ChequeID = models.CharField(max_length=50, primary_key=True)
#     PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='cheque')
#     ChequeNo = models.CharField(max_length=50)
#     BankCheque = models.CharField(max_length=100)
#     NameCheque = models.CharField(max_length=100)

#     def __str__(self):
#         return f"Cheque {self.ChequeNo}"
