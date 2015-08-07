# coding: utf8

from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views

urlpatterns = [
    # urls d'authentification
    url(
        '^connexion/$',
        auth_views.login,
        {
            'template_name': 'connexion.html',
            'extra_context': {'next': '/'},
        },
        name='connexion',
    ),
    url(
        '^deconnexion/$',
        auth_views.logout_then_login,
        name='deconnexion',
    ),

    # urls de bank home
    url(r'^', include('comptes.urls')),

    # urls de l'admin
    url(r'^admin/', include(admin.site.urls)),
]
