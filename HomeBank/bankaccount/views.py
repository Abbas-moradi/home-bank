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
        ser_data = BankAccountSerializers(instance=request.POST)
        if ser_data.is_valid():
            Account.objects.create(**ser_data.data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class BankAcoountUpdateApiView(APIView):

    def put(self, request, pk):
        pass


class BankAcoountDeleteApiView(APIView):

    def delete(self, request, pk):
        pass