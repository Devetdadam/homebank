# coding: utf8

from django.conf.urls import url

from .views import AccueilTemplateView, AdministrationListView,\
    CompteCreateView, CompteUpdateView,\
    CategorieCreateView, CategorieUpdateView,\
    MetacategorieCreateView, MetacategorieUpdateView

urlpatterns = [
    # ACCUEIL
    url(r'^$',
        AccueilTemplateView.as_view(),
        name='accueil'),

    # ADMINISTRATION
    url(r'^administration/$',
        AdministrationListView.as_view(),
        name='administration'),

    # COMPTES
    url(r'^comptes/nouveau/$',
        CompteCreateView.as_view(),
        name='compte_create'),
    url(r'^comptes/modifier/(?P<alias>.+)/$',
        CompteUpdateView.as_view(),
        name='compte_update'),

    # METACATEGORIES
    url(r'^metacategorie/nouvelle/$',
        MetacategorieCreateView.as_view(),
        name='metacategorie_create'),

    url(r'^metacategorie/modifier/(?P<metacategorie>.+)/$',
        MetacategorieUpdateView.as_view(),
        name='metacategorie_update'),

    # CATEGORIES
    url(r'^categorie/nouvelle-categorie-dans-(?P<metacategorie>.+)/$',
        CategorieCreateView.as_view(),
        name='categorie_create'),


]
