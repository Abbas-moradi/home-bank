from rest_framework import serializers
from bankaccount.models import Account, Transaction, AccountTransaction
from loan.serializers import LoanSerializers
from loan.models import LoanTransaction


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


class TransactionSerializers(serializers.ModelSerializer):
    account_transaction = serializers.SerializerMethodField()
    loan_transaction = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = '__all__'

    def get_account_transaction(self, obj):
        result = obj.account.all()
        return AccountTransactionSerializers(instance=result, many=True).data

    def get_loan_transaction(self, obj):
        result = obj.loan.all()
        return LoanTransactionSerializers(instance=result, many=True).data


class AccountTransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = AccountTransaction
        fields = '__all__'


class LoanTransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = LoanTransaction
        fields = '__all__'