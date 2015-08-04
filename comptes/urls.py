# coding: utf8

from django.conf.urls import url

from .views import AccueilTemplateView

urlpatterns = [
    # page d'accueil
    url(r'^accueil/',
        AccueilTemplateView.as_view(),
        name='accueil'),
]
