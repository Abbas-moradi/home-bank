from django.contrib import admin
from loan.models import Loan, LoanTransaction


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'start_date', 'loan_amount', 'end_date', 'loan_remaining']


@admin.register(LoanTransaction)
class LoanTransactionAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'loan', 'amount_installment', 
                    'date', 'status', 'loan_balance']

