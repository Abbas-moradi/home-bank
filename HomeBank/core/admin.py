from django.contrib import admin
from core.models import Branch, BranchSetting


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['salary', 'count', 'cost', 'wage']

