# coding: utf8

from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .models import Compte


class AccueilTemplateView(TemplateView):
    """page d'accueil de l'application"""
    template_name = "comptes/accueil.html"


# Vues du modèle Compte
class CompteListView(ListView):
    """Liste des comptes créés"""
    model = Compte
    template_name = 'comptes/comptes_list.html'


