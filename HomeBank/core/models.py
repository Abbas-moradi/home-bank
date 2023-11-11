from django.db import models


class BranchSetting(models.Model):
    tution = models.IntegerField(default=0)
    loan_amount = models.IntegerField()
    installment_number = models.PositiveSmallIntegerField(default=1)
    wage = models.IntegerField()
    bank_email = models.EmailField(max_length=250)
    bank_card_number = models.CharField(max_length=16)
    description = models.TextField()
    sms_fee = models.PositiveSmallIntegerField(default=250)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'Setting'
        ordering = ('id', )


class Branch(models.Model):
    salary = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    cost = models.PositiveIntegerField(default=0)
    wage = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = 'branch'
        ordering = ('id', )