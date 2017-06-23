from rest_framework import viewsets
from .models import Account, SubAccount, SubSubAccount
from .serializers import AccountSerializer

# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
