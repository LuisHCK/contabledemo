from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Account, SubAccount, SubSubAccount
from .serializers import AccountSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# Account Model CRUD


@csrf_exempt
def newAccount(request):
    # This view creates a new Account.
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def listAccounts(request):
    # This view lists the Account model existing objetcs.
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(
            serializer.data, safe=False,
            json_dumps_params={'indent': 2})


@csrf_exempt
def rudAccount(request, pk):
    # This view reads, updates or deletes an Account
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=404)
    # Reads
    if request.method == 'GET':
        serializer = AccountSerializer(account, many=False)
        return JsonResponse(
            serializer.data, safe=False,
            json_dumps_params={'indent': 2}
        )
    # Updates
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(account, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        account.delete()
        return HttpResponse(status=204)


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
                "AccountID": account.id, "AccountName": account.name,
                "Category": account.category.name}
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
