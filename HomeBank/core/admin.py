from django.contrib import admin
from core.models import Branch, BranchSetting, Request


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('salary', 'count', 'cost', 'wage')


@admin.register(BranchSetting)
class BranchSettingAdmin(admin.ModelAdmin):
    list_display = ('tution', 'loan_amount', 'installment_number', 
                    'wage', 'bank_email', 'bank_card_number',
                    'description', 'sms_fee')
    

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request', 'description', 'created', 'seen', 'user')