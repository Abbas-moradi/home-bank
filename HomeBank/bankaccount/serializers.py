from rest_framework import serializers
from bankaccount.models import Account


class BankAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class BankAccountUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('balance', )