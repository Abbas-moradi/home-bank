from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('users/', UserRegisterApiView.as_view(), name='users'),
    path('register/', UserRegisterApiView.as_view(), name='register'),
    path('update/<str:pk>/', UserRegisterApiView.as_view(), name='update'),
    path('delete/<str:pk>/', UserRegisterApiView.as_view(), name='delete'),
]