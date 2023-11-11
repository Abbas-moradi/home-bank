from django.shortcuts import render
from rest_framework.views import APIView
from loan.models import Loan
from loan.serializers import LoanSerializers
from rest_framework.response import Response
from rest_framework import status


class LoansApiView(APIView):

    def get(self, request):
        loans = Loan.objects.filter(status=True, termination=False)
        ser_data = LoanSerializers(instance=loans, many=True)    
        return Response(ser_data.data, status=status.HTTP_200_OK)
       

