from django.db import models


class BranchSetting(models.Model):
    tution = models.IntegerField(default=0)
    Installment_number = models.PositiveSmallIntegerField(default=1)
    percent = models.DecimalField(default=1.0)
    bank_email = models.EmailField(max_length=250)
    bank_card_number = models.CharField(max_length=16)
    description = models.TextField()
    sms_fee = models.PositiveSmallIntegerField(default=250)

    def __str__(self) -> str:
        return self.id
    
    class Meta:
        vebose_name = 'setting'
        verbose_name_plural = 'Setting'
        ordering = 'id'
