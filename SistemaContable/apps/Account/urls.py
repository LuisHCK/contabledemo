from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    url(r'^$', views.getAccountsStructure, name='getAccountsStructure'),
    url(r'account', views.listAccounts, name='listAccounts'), ]
