from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.getAccountsStructure, name='getAccountsStructure'),
    url(r'account/^$', views.listAccounts, name='listAccounts'),
    url(r'account/new/^$', views.newAccount, name='newAccount'),
    url(r'account/(?P<pk>[0-9]+)/$', views.rudAccount,
        name='rudAccout'),
     ]
