from rest_framework import serializers
from bankaccount.models import Account
from loan.serializers import LoanSerializers


class BankAccountSerializers(serializers.ModelSerializer):
    loan = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_loan(self, obj):
        result = obj.loan.filter(termination=False, status=True)
        return LoanSerializers(instance=result, many=True).data


class BankAccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('balance', )