from collections.abc import Iterable
from django.db import models
from bankaccount.models import Account, Transaction
from datetime import timedelta, datetime
from core.models import BranchSetting


class Loan(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='loan')
    start_date = models.DateField(auto_now_add=True)
    loan_amount = models.IntegerField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    wage_amount = models.IntegerField(null=True, blank=True)
    term = models.IntegerField(null=True, blank=True)
    installment_number = models.PositiveSmallIntegerField(null=True, blank=True)
    installment_amount = models.PositiveIntegerField(null=True, blank=True)
    delay_days = models.PositiveSmallIntegerField(default=0)
    installment_paid = models.IntegerField(default=0, null=True, blank=True)
    loan_remaining = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    termination = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'
        ordering = ('start_date', )
    
    def __str__(self) -> str:
        return str(self.id)
    
    def save(self) -> None:
        
        if self.installment_paid == self.term:
            self.loan_remaining = (self.installment_amount*self.installment_paid) - self.loan_amount    
            self.termination = True
            self.status = False
            self.account.loan_status = True
            self.account.save()
        else:
            self.loan_remaining = (self.installment_amount*self.installment_paid) - self.loan_amount    
        return super().save()
    
    def initial_setting(self):
        setting = BranchSetting.objects.get(pk=1)
        self.term = setting.installment_number
        self.installment_number = setting.installment_number
        self.loan_amount = setting.loan_amount
        self.end_date = datetime.now() + timedelta(days=30 * self.term)
        self.installment_amount = self.loan_amount / self.term
        self.wage_amount = setting.wage
        self.loan_remaining = 0 - self.loan_amount
        self.account.loan_status = False
        self.account.save()
    
        return super().save()
    

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
        return str(self.id)
