from rest_framework import serializers
from loan.models import Loan


class LoanSerializers(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'