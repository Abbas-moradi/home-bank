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
        fields = ('national_code', 'full_name', 'phone', 'email', 'sex', 'password', 'password2')
        extra_kwargs = {
            'password':{'write_only':True},
            }
        
    def validate(self, data):
        if 'admin' in data['full_name']:
            raise serializers.ValidationError('Admin cannot be in full name')
        if 'admin' in data['email']:
            raise serializers.ValidationError('Admin cannot be in email')
        if len(data['national_code']) != 10:
            raise serializers.ValidationError('national code must be 10 number length.')
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Password verification does not match.')
        if 'sex' in ('M', 'W'):
            raise serializers.ValidationError('Gender(sex) must be M or W')
        return data
    
    def create(self, validated_data):
        del validated_data['password2']
        print(validated_data)
        return User.objects.create(**validated_data)