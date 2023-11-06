from django.contrib import admin
from core.models import Branch, BranchSetting


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['salary', 'count', 'cost', 'wage']


@admin.register(BranchSetting)
class BranchSettingAdmin(admin.ModelAdmin):
    list_display = ['tution', 'Installment_number', 
                    'percent', 'bank_email', 'bank_card_number',
                    'description', 'sms_fee']