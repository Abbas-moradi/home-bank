from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from bankaccount.models import Account, AccountTransaction, Transaction
from bankaccount.serializers import BankAccountSerializers, BankAccountUpdateSerializers
from bankaccount.serializers import TransactionSerializers, AccountTransactionSerializers
from loan.serializers import LoanTransactionSerializers
from core.models import BranchSetting
from loan.models import Loan, LoanTransaction
from accounts.models import User
from datetime import datetime
from django.db.models import Q


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
            account_id = [id for id in user_accounts]
            user_loans = []
            loans = []
            for _ in user_accounts:
                if _.loan_status == False:
                    loans.append(Loan.objects.get(account=_, termination=False, status=True))
                    user_loans.append(Loan.objects.filter(account=_, termination=False, status=True).values_list('installment_amount', flat=False))

            installment_amounts = [item[0] for item in user_loans if item]
            total_installment_amounts = sum(item[0] for item in installment_amounts)
            if int(total_installment_amounts + sum_user_account_tution) == int(amount):
                user = get_object_or_404(User, pk=user_id_in)
                trans = Transaction.objects.create(user=user, amount=amount, 
                                        description=f'accounts={user_accounts} - loans={loans}',
                                        receipt_code=receipt_code)
                
                for loan in loans:
                    loan_data = Loan.objects.get(pk=loan.id)
                    loan_data.installment_paid += 1
                    loan_data.save()
                    LoanTransaction.objects.create(
                        transaction=trans,
                        loan=loan,
                        amount_installment=loan.installment_amount,
                        loan_balance=loan.loan_remaining
                    )
                
                for ac in user_accounts:
                    ac.balance += tution.tution
                    ac.save()
                    AccountTransaction.objects.create(
                        transaction = trans,
                        account = ac,
                        account_amount = tution.tution,
                        account_balance = ac.balance,
                    )

                    
                ser_deta = TransactionSerializers(instance=trans)

                return Response(ser_deta.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'amount errore': 'The deposit amount is not equal to the amount that the user has to deposit'})


class TotalBalanceOfAccountsApiView(APIView):
    """ in this API you can see total accounts balance  """
    def get(self, request):
        totalbalance = 0
        totalaccounts = Account.objects.all()
        for account in totalaccounts:
            totalbalance += account.balance
        context = {'total balance': totalbalance}
        return Response(context, status=status.HTTP_200_OK)


class AccountBillingApiView(APIView):
    """ You can see the invoice of a specific account
        using a certain period of time in this API 
        The date format should be like this -> '2023-11-13' """

    def post(self, request):
        account = Account.objects.get(pk=request.POST['account'])
        start_date = request.POST['start']
        end_date = request.POST['end']
        
        if datetime.strptime(start_date, "%Y-%m-%d") > datetime.strptime(end_date, "%Y-%m-%d"):
            return Response({'Date Errore': 'The start date cannot be greater than the end date'}
                            , status=status.HTTP_400_BAD_REQUEST)
        
        ac_tr = AccountTransaction.objects.filter(
            Q(account=account) & Q(date__gte=start_date) & Q(date__lte=end_date))
        
        try:
            loan = get_object_or_404(Loan, account=account, termination=False)
            lo_tr = LoanTransaction.objects.filter(
                Q(loan=loan) & Q(date__gte=start_date) & Q(date__lte=end_date))
            loan_result=True
        except:
            loan_result = False

        if len(ac_tr)>0 and loan_result==True:
            ac_ser_data = AccountTransactionSerializers(instance=ac_tr, many=True)
            lo_ser_data = LoanTransactionSerializers(instance=lo_tr, many=True)
            return Response((ac_ser_data.data, lo_ser_data.data), status=status.HTTP_200_OK)
        return Response({'result': 'There are no transactions in this time frame'}, status=status.HTTP_404_NOT_FOUND)
            
        

        
