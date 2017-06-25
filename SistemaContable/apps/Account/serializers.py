from rest_framework import serializers
from .models import Account, SubAccount, SubSubAccount


class AccountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ('id', 'name', 'category')


class SubAccountSerializer(serializers.ModelSerializer):
	account = serializers.StringRelatedField()

	class Meta:
		model = SubAccount
		fields = ('id', 'name', 'account')
