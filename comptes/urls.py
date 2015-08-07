# coding: utf8

from django.conf.urls import url

from .views import AccueilTemplateView, AdministrationListView,\
    CompteCreateView, CompteUpdateView,\
    CategorieCreateView, CategorieUpdateView

urlpatterns = [
    # page d'accueil
    url(r'^$',
        AccueilTemplateView.as_view(),
        name='accueil'),

    # administration des comptes, categories et lignes
    url(r'^administration/$',
        AdministrationListView.as_view(),
        name='administration'),

    url(r'^comptes/nouveau/$',
        CompteCreateView.as_view(),
        name='compte_create'),
    url(r'^comptes/modifier/(?P<alias>.+)/$',
        CompteUpdateView.as_view(),
        name='compte_update'),

    url(r'^categorie/nouveau/$',
        CategorieCreateView.as_view(),
        name='categorie_create'),
    url(r'^categorie/modifier/(?P<categorie>.+)/$',
        CategorieUpdateView.as_view(),
        name='categorie_update'),
]
