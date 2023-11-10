from django.urls import path
from loan.views import *


app_name = 'loan'


urlpatterns = [
    path('loans/', LoansApiView.as_view(), name='loans'),
]