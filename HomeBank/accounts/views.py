from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer, UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User


class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        ser_data = UserSerializer(instance=users, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    

class UserRegisterApiView(APIView):

    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            User.objects.create(
                national_code = ser_data.validated_data['national_code'],
                email = ser_data.validated_data['email'],
                full_name = ser_data.validated_data['full_name'],
                phone = ser_data.validated_data['phone'],
                password = ser_data.validated_data['password'],
            )
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
