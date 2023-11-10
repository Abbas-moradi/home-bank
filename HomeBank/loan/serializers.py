from rest_framework.serializers import Serializer
from loan.models import Loan


class LoanSerializers(Serializer):
    class Meta:
        model = Loan
        fields = '__all__'