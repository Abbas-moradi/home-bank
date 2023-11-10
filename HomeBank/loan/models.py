from django.db import models
from bankaccount.models import Account, Transaction


class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    loan_amount = models.IntegerField()
    end_date = models.DateField(null=True)
    wag_amount = models.IntegerField()
    term = models.IntegerField()
    installment_number = models.PositiveSmallIntegerField()
    delay_days = models.PositiveSmallIntegerField(default=0)
    installment_paid = models.IntegerField()
    status = models.BooleanField(default=True)
    termination = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'
        ordering = ('start_date', )
    
    def __str__(self) -> str:
        return self.id
    

class LoanTransaction(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount_installment = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    loan_balance = models.IntegerField()

    class Meta:
        verbose_name = 'LoanTransaction'
        verbose_name_plural = 'LoanTransactions'
        ordering = ('date', )

    def __str__(self) -> str:
        return self.id
