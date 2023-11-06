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

    def set_closed_date(self):
        from datetime import date
        if self.closed:
            self.closed_date = date.today()
        else:
            self.closed_date = None
    

