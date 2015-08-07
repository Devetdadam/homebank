# coding: utf8

from django.conf.urls import url

from .views import AccueilTemplateView,\
    CompteListView, CompteCreateView, CompteUpdateView

urlpatterns = [
    # page d'accueil
    url(r'^$',
        AccueilTemplateView.as_view(),
        name='accueil'),

    # gestion des comptes
    url(r'^comptes/$',
        CompteListView.as_view(),
        name='comptes_list'),
    url(r'^comptes/nouveau/$',
        CompteCreateView.as_view(),
        name='compte_create'),
    url(r'^comptes/modifier/(?P<alias>.+)/$',
        CompteUpdateView.as_view(),
        name='compte_update'),
]
