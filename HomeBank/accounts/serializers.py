from rest_framework import serializers
from accounts.models import User
from bankaccount.models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        models = User
        fields = ('national_code', 'full_name', 'phone', 'email', 'password', 'password2')
        extra_kwargs = {
            'password':{'write_only':True},
            }