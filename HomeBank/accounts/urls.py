from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('users/', UserApiView.as_view(), name='users'),
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('update/<str:pk>/', UserUpdateApiView.as_view(), name='update'),
    path('delete/<str:pk>/', UserDeleteApiView.as_view(), name='delete'),
]