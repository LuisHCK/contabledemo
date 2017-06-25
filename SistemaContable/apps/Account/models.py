from django.db import models

# Create your models here.


class AccountCategory(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=150)
    category = models.OneToOneField(AccountCategory)

    def __str__(self):
    	return self.name

class SubAccount(models.Model):
    name = models.CharField(max_length=150)
    account = models.ForeignKey(Account)
    
    def __str__(self):
    	return self.name

class SubSubAccount(models.Model):
    name = models.CharField(max_length=150)
    subAccount = models.ForeignKey(SubAccount)
    
    def __str__(self):
    	return self.name
