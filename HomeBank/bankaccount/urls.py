from django.urls import path
from bankaccount.views import *


app_name = 'bankaccounts'

urlpatterns = [
    path('allaccounts/', BankAcoounts.as_view(),name='bankaccounts'),
]