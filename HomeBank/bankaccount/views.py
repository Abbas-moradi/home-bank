from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from bankaccount.models import Account, AccountTransaction, Transaction
from bankaccount.serializers import BankAccountSerializers, BankAccountUpdateSerializers


class BankAccountsApiView(APIView):

    def get(self, request):
        bac = Account.objects.all()
        ser_data = BankAccountSerializers(instance=bac, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class BankAccountCreateApiView(APIView):

    def post(self, request):
        ser_data = BankAccountSerializers(data=request.POST)
        if ser_data.is_valid():
            Account.objects.create(**ser_data.data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class BankAccountUpdateApiView(APIView):

    def put(self, request, pk):
        try:
            bankAccount = Account.objects.get(pk=pk, closed=False)
            ser_data = BankAccountUpdateSerializers(instance=bankAccount, data=request.data, partial=True)
            if ser_data.is_valid():
                bankAccount.balance += int(request.POST['balance'])
                bankAccount.save()
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'account not found or closed': pk}, status=status.HTTP_404_NOT_FOUND)


class BankAccountDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            bankAccount = get_object_or_404(Account, pk=pk, closed=False)
            ser_data = BankAccountSerializers(instance=bankAccount)
            if bankAccount.balance != 0:
                return Response({'account balance not equal 0':ser_data.data}, status=status.HTTP_406_NOT_ACCEPTABLE)
            elif bankAccount.loan_status==True:
                return Response({'account have loan': ser_data.data}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                bankAccount.closed = True
                bankAccount.save()
                return Response({'account closed': ser_data.data}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'account not found or closed': pk}, status=status.HTTP_404_NOT_FOUND)