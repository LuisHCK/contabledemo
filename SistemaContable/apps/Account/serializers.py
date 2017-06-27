from rest_framework import serializers
from .models import Account, SubAccount, SubSubAccount, AccountCategory


class AccountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ('id', 'name', 'category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCategory
        fields = ('id', 'name')

class SubAccountSerializer(serializers.ModelSerializer):
	account = serializers.StringRelatedField()

	class Meta:
		model = SubAccount
		fields = ('id', 'name', 'account')
