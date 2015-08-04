# coding: utf8

from django.conf.urls import url
from .views import AccueilTemplateView
from .views import CompteListView

urlpatterns = [
    # page d'accueil
    url(r'^accueil/',
        AccueilTemplateView.as_view(),
        name='accueil'),

    # liste des comptes
    url(r'^comptes/',
        CompteListView.as_view(),
        name='comptes-list'),
]
