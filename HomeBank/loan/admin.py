from django.contrib import admin
from loan.models import Loan, LoanTransaction


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['account', 'start_date', 'loan_amount', 'end_date']
    
