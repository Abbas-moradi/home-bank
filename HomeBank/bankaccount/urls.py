from django.urls import path
from bankaccount.views import *


app_name = 'bankaccounts'

urlpatterns = [
    path('allaccounts/', BankAccountsApiView.as_view(),name='bankaccounts'),
    path('createaccount/', BankAccountCreateApiView.as_view(),name='createaccount'),
    path('updateaccount/<str:pk>/', BankAccountUpdateApiView.as_view(),name='updateaccount'),
    path('deleteaccount/<str:pk>/', BankAccountDeleteApiView.as_view(),name='deleteaccount'),
]