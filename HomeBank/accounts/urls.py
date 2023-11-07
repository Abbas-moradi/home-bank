from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('users/', UserApiView.as_view(), name='users'),
    path('register/', UserRegisterApiView.as_view(), name='register'),
]