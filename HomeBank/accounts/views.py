from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer, UserRegisterSerializer, UserUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
    

class UserApiView(APIView):
    """ In this urls you can view the all users """

    def get(self, request):
        users = User.objects.all()
        ser_data = UserSerializer(instance=users, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class UserCreateApiView(APIView):
    """ In this urls you can created user """
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateApiView(APIView):
    """  In this urls you can update user """
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        ser_data = UserUpdateSerializer(instance=user, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteApiView(APIView):
    """ In this urls you can theleted user, 
        when deleted user, user is_active field equal False """
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        if user.is_active == False:
            return Response({'result':'user not found.'}, status=status.HTTP_404_NOT_FOUND)
        ser_data = UserUpdateSerializer(instance=user, data={'is_active':False}, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_202_ACCEPTED)
        
