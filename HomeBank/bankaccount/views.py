from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from bankaccount.models import Account, AccountTransaction, Transaction
from bankaccount.serializers import BankAccountSerializers, BankAccountUpdateSerializers
from bankaccount.serializers import TransactionSerializers
from core.models import BranchSetting
from loan.models import Loan
from accounts.models import User
import uuid


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
        branch_setting = BranchSetting.objects.get(pk=1) 
        try:
            bankAccount = Account.objects.get(pk=pk, closed=False)
            ser_data = BankAccountUpdateSerializers(instance=bankAccount, data=request.data, partial=True)
            if ser_data.is_valid():
                bankAccount.balance += branch_setting.tution
                bankAccount.save()
                account = Account.objects.get(pk=bankAccount.id)
                serializ = BankAccountSerializers(instance=account)
                return Response(serializ.data, status=status.HTTP_200_OK)
            return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'account not found or closed': pk}, status=status.HTTP_404_NOT_FOUND)


class BankAccountDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            bankAccount = get_object_or_404(Account, pk=pk, closed=False)
            ser_data = BankAccountSerializers(instance=bankAccount)
            if bankAccount.balance != 0:
                return Response({'account balance not equal 0':ser_data.data}, 
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            elif bankAccount.loan_status==True:
                return Response({'account have loan': ser_data.data}, 
                                status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                bankAccount.closed = True
                bankAccount.save()
                return Response({'account closed': ser_data.data}, 
                                status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'account not found or closed': pk}, 
                            status=status.HTTP_404_NOT_FOUND)
        

class TransactionApiView(APIView):

    def get(self, request):
        tr = Transaction.objects.all()
        ser_data = TransactionSerializers(instance=tr, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    

class TransactionCreateApiView(APIView):

    def post(self, request):
        amount = request.POST['amount']
        user_id_in = request.POST['user']
        receipt_code = request.POST['receipt_code']
        try:
            registered = get_object_or_404(Transaction, receipt_code=receipt_code, status=True)
            return Response({'result': 'Receipt already registered'})
        except:
        
            user_accounts = []
            for _ in Account.objects.filter(user=user_id_in, status=True, closed=False):
                user_accounts.append(_)

            tution = BranchSetting.objects.get(pk=1)
            sum_user_account_tution = len(user_accounts)*tution.tution
            user_id = [id for id in user_accounts]
            user_loans = []
            loans = []
            for _ in user_id:
                user_loans.append(Loan.objects.filter(account=_, termination=False, status=True).values_list('installment_amount', flat=False))
                loans.append(Loan.objects.get(account=_, termination=False, status=True))
            
            installment_amounts = [item[0] for item in user_loans if item]
            total_installment_amounts = sum(item[0] for item in installment_amounts)
            if int(total_installment_amounts + sum_user_account_tution) == int(amount):
                user = get_object_or_404(User, pk=user_id_in)
                trans = Transaction.objects.create(user=user, amount=amount, 
                                        description=f'accounts={user_accounts} - loans={loans}',
                                        receipt_code=receipt_code)
                ser_deta = TransactionSerializers(instance=trans)

                return Response(ser_deta.data, status=status.HTTP_201_CREATED)
            return Response({'amount errore': 'The deposit amount is not equal to the amount that the user has to deposit'})