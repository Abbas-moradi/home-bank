from django.urls import path
from bankaccount.views import *


app_name = 'bankaccounts'

urlpatterns = [
    path('allaccounts/', BankAcoountsApiView.as_view(),name='bankaccounts'),
    path('allaccounts/', BankAcoountsApiView.as_view(),name='bankaccounts'),
]