from django.shortcuts import render
from rest_framework.views import APIView
from loan.models import Loan
from loan.serializers import LoanSerializers
from rest_framework.response import Response
from rest_framework import status
from bankaccount.models import Account
from django.shortcuts import get_object_or_404
from accounts.models import User


class LoansApiView(APIView):

    def get(self, request):
        loans = Loan.objects.all()
        ser_data = LoanSerializers(instance=loans, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    
class LoanCreateApiView(APIView):
    
    def post(self, request):
        account = get_object_or_404(Account, pk=request.POST['account'],
                                    status=True, closed=False)
        
        if account.loan_status == False:
            return Response({'result': 'account have loan'})

        user = get_object_or_404(User, pk=request.POST['id'])
        user_accounts = Account.objects.filter(user=user).values_list('id', flat=True)

        for ua in user_accounts:
            try:
                loan = get_object_or_404(Loan, account=ua, termination=False)
                if loan and loan.termination==False and loan.delay_days > 0:
                    return Response({'result': 'The user has a delay in payment'}, 
                                    status=status.HTTP_406_NOT_ACCEPTABLE)
            except:
                continue
    
        loan_instance = Loan(account=account)
        loan_instance.initial_setting()
        account.loan_status = False
        account.save()
        get_loan = Loan.objects.get(pk=loan_instance.id)
        loan_paid = LoanSerializers(instance=get_loan)
        return Response(loan_paid.data, 
                        status=status.HTTP_201_CREATED)


class LoanUpdateApiView(APIView):

    def put(self, request, pk):
        try:
            loan = get_object_or_404(Loan, pk=pk, termination=False)
            if loan != None:
                loan.installment_paid += 1
                loan.save()
                loan_result_show = Loan.objects.get(pk=pk)
                ser_data = LoanSerializers(instance=loan_result_show)
                return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'result':'loan not found or settled'}, status=status.HTTP_404_NOT_FOUND)