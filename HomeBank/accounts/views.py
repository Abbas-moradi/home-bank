from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User


class UserApiView(APIView):
    def get(self):
        users = User.objects.all()
        ser_data = UserSerializer(instance=users, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
