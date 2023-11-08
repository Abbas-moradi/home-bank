from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('users/', UserApiView.as_view(), name='users'),
    path('register/', UserApiView.as_view(), name='register'),
    path('update/<str:pk>/', UserApiView.as_view(), name='update'),
    path('delete/<str:pk>/', UserApiView.as_view(), name='delete'),
]