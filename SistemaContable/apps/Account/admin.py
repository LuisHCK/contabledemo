from django.contrib import admin
from .models import AccountCategory, Account, SubAccount, SubSubAccount

admin.site.register(AccountCategory)
admin.site.register(Account)
admin.site.register(SubAccount)
admin.site.register(SubSubAccount)
