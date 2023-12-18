from rest_framework import serializers
from loan.models import Loan, LoanTransaction


class LoanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'


class LoanTransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = LoanTransaction
        fields = '__all__'