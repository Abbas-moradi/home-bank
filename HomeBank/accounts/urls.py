from django.urls import path, include
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('', UserApiView.as_view(), name='users'),
]