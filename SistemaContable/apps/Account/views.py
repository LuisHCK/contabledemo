from rest_framework import viewsets
from .models import Account, SubAccount, SubSubAccount
from .serializers import AccountSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def listAccounts(request):
    # This view lists the Account model existing objetcs.
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(
            serializer.data, safe=False,
            json_dumps_params={'indent': 2})


def getAccountsStructure(request):
    """ This view gets the whole structure of the account app and returns json.
    It loops through each account, subaccount, subsubaccount to create the json
    file
    """
    account_structure = []
    subaccountsList = []
    subsubaccountsList = []
    if request.method == 'GET':
        accounts = Account.objects.all()
        for account in accounts:
            accountData = {
                "AccountID": account.id, "AccountName": account.name}
            subaccounts = SubAccount.objects.filter(account=account)
            for subaccount in subaccounts:
                subaccountData = {
                    "SubAccountID": subaccount.id,
                    "SubAccountName": subaccount.name
                }
                subsubaccounts = SubSubAccount.objects.filter(
                    subAccount=subaccount)
                for subsubaccount in subsubaccounts:
                    subsubaccountData = {
                        "SubSubAccountID": subsubaccount.id,
                        "SubSubAccountName": subsubaccount.name}
                    subsubaccountsList.append(subsubaccountData)
                    subaccountData["SubSubAccounts"] = subsubaccountsList
                subaccountsList.append(subaccountData)
                accountData["SubAccounts"] = subaccountsList
            account_structure.append(accountData)
        return JsonResponse(
            account_structure, safe=False, json_dumps_params={'indent': 2})


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
