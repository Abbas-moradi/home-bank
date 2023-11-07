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
        model = User
        fields = ('national_code', 'full_name', 'phone', 'email', 'password', 'password2')
        extra_kwargs = {
            'password':{'write_only':True},
            }
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password confirm dont match.')
        if 'admin' in data['email']:
            raise serializers.ValidationError('`admin` not in email.')
        if 'admin' in data['full_name']:
            raise serializers.ValidationError('`admin` not in full name.')
        return data