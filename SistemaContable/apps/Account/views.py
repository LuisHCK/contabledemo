from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Account, SubAccount, SubSubAccount, AccountCategory
from .serializers import AccountSerializer, SubAccountSerializer, CategorySerializer
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
        data = JSONParser().parse(request)
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            #get category from request
            try:
                # if user pick a category get the id and get the category instance
                # and pass to serializer and save
                category = AccountCategory.objects.get(pk=int(data['category_id']))
                serializer.save(category=category)
            except:
                # else save account without a category
                serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listCategories(request):
    "List all categories for accounts"
    categories = AccountCategory.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(
        serializer.data, safe=False,
    )


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

    # Deletes
    elif request.method == 'DELETE':
        account.delete()
        return HttpResponse(status=204)


# Sub Account model CRUD


def newSubAccount(request):
    # This view creates a new SubAccount
    if request.method == 'POST':
        serializer = SubAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, status=status.HTTP_400_BAD_REQUEST)    


@csrf_exempt
def listSubAccounts(request):
    # This view lists the Account model existing objetcs.
    if request.method == 'GET':
        subAccounts = SubAccount.objects.all()
        serializer = SubAccountSerializer(subAccounts, many=True)
        return JsonResponse(
            serializer.data, safe=False,
            json_dumps_params={'indent': 2})


def rudSubAccount(request, pk):
    # This view reads, updates or deletes a SubAccount
    try:
        subaccount = SubAccount.objects.get(pk=pk)
    except SubAccount.DoesNotExist:
        return HttpResponse(status=404)

    # Reads
    if request.method == 'GET':
        serializer = SubAccountSerializer(subaccount, many=False)
        return JsonResponse(
            serializer.data, safe=False,
            json_dumps_params={'indent': 2})
    # Updates
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccountSerializer(Account, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data, safe=False,
                json_dumps_params={'indent': 2}
                )
    # Deletes
    if request.method == 'DELETE':
        account.delete()
        return HttpResponse(staus=204)


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
                # don't get category to avoid NoneType exception
                #"Category": account.category.name
                }
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
