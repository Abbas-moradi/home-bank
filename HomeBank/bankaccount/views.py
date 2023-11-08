from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bankaccount.models import Account, AccountTransaction, Transaction
from bankaccount.serializers import BankAccountSerializers


class BankAcoountsApiView(APIView):

    def get(self, request):
        bac = Account.objects.all()
        ser_data = BankAccountSerializers(instance=bac, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class BankAcoountCreateApiView(APIView):

    def post(self, request):
        pass