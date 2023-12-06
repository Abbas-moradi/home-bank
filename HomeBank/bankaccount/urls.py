from django.urls import path
from bankaccount.views import *


app_name = 'bankaccounts'

urlpatterns = [
    path('allaccounts/', BankAccountsApiView.as_view(),name='bankaccounts'),
    path('transactions/', TransactionApiView.as_view(),name='transactions'),
    path('createtransaction/', TransactionCreateApiView.as_view(),name='createtransaction'),
    path('createaccount/', BankAccountCreateApiView.as_view(),name='createaccount'),
    path('updateaccount/<str:pk>/', BankAccountUpdateApiView.as_view(),name='updateaccount'),
    path('deleteaccount/<str:pk>/', BankAccountDeleteApiView.as_view(),name='deleteaccount'),
    path('totalbalance/', TotalBalanceOfAccountsApiView.as_view(),name='totalbalance'),
]