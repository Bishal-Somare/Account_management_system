from django.contrib import admin
from .models import Transaction, Payment, CreditCard, Cash

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['TransactionID', 'AccountID', 'DateOfTransaction', 'BankName', 'Debit', 'Credit', 'TotalAmount']
    list_filter = ['DateOfTransaction', 'BankName']
    search_fields = ['TransactionID', 'Description']
    date_hierarchy = 'DateOfTransaction'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['PaymentID', 'TransactionID', 'Currency', 'Amount']
    list_filter = ['Currency']
    search_fields = ['PaymentID']

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['CreditCardNo', 'PaymentID', 'BankCredit', 'NameCredit']
    search_fields = ['CreditCardNo', 'NameCredit']

@admin.register(Cash)
class CashAdmin(admin.ModelAdmin):
    list_display = ['CashTransactionNo', 'PaymentID', 'NameCash', 'CashTendered']
    search_fields = ['CashTransactionNo', 'NameCash']
