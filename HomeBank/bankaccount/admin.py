from django.contrib import admin
from bankaccount.models import Account, AccountTransaction, Transaction


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'account_number', 'balance', 
                    'opening_date', 'loan_status', 'status',
                    'closed', 'closed_date']

@admin.register(AccountTransaction)
class AccountTransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'account',
                    'account_amount', 'account_balance',
                    'date', 'status', 'on_delete']
