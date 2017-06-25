from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Account
        fields = ('id', 'name', 'category')
