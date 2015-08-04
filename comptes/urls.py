# coding: utf8

from django.conf.urls import url
from .views import ComptesListView

urlpatterns = [
    url(r'^comptes/', CompteListView.as_view(), name='compte_list'),
]
