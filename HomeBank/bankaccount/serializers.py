from rest_framework import serializers
from bankaccount.models import Account


class BankAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
        