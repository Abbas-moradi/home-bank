from django.db import models
from accounts.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.PositiveIntegerField()
    balance = models.IntegerField()
    opening_date = models.DateField(auto_now_add=True)
    loan_status = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    closed_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ('account_number', )

    def set_closed_date(self):
        from datetime import date
        if self.closed:
            self.closed_date = date.today()
        else:
            self.closed_date = None

    def __str__(self) -> str:
        return self.id
    

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    receipt = models.IntegerField()
    status = models.BooleanField(default=True)
    record = models.BooleanField(default=False)
    record_date = models.DateField(null=True)
    on_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
        ordering = ('registration_date', )

    def set_record_date(self):
        from datetime import date
        if self.record:
            self.record_date = date.today()
        else:
            self.record_date = None

    def __str__(self) -> str:
        return self.id


class AccountTransaction(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    account_amount = models.IntegerField()
    account_balance = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    on_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'AccountTransaction'
        verbose_name_plural = 'AccountTransactions'
        ordering = ('date', )

    def __str__(self)-> str:
        return self.id


