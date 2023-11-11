from django.shortcuts import render
from rest_framework.views import APIView
from loan.models import Loan
from loan.serializers import LoanSerializers
from rest_framework.response import Response
from rest_framework import status
from bankaccount.models import Account
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout


class LoansApiView(APIView):

    def get(self, request):
        loans = Loan.objects.filter(status=True, termination=False)
        ser_data = LoanSerializers(instance=loans, many=True)    
        return Response(ser_data.data, status=status.HTTP_200_OK)
    
class LoanCreateApiView(APIView):
    
    def post(self, request):
        account = get_object_or_404(Account, pk=request.POST['account'],
                                    status=True, closed=False)
        if account.loan_status == False:
            return Response({'result': 'account have loan'})
    
        loan_instance = Loan(account=account)
        loan_instance.save()
        account.loan_status = False
        account.save()
        return Response({'status':'loan paid'}, 
                        status=status.HTTP_201_CREATED)


