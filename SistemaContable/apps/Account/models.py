from django.db import models

# Create your models here.


class AccountCategory(models.Model):
    name = models.CharField(max_length=15)


class Account(models.Model):
    name = models.CharField(max_length=150)
    category = models.OneToOneField(AccountCategory)


class SubAccount(models.Model):
    name = models.CharField(max_length=150)
    account = models.ForeignKey(Account)


class SubSubAccount(models.Model):
    name = models.CharField(max_length=150)
    subAccount = models.ForeignKey(SubAccount)
