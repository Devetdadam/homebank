# coding: utf8

from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .models import Compte, Metacategorie


# Page d'Accueil
class AccueilTemplateView(TemplateView):
    """page d'accueil de l'application"""
    template_name = "comptes/accueil.html"


# Vues du modèle Compte
class CompteListView(ListView):
    """Liste des comptes créés"""
    model = Compte
    template_name = 'comptes/comptes_list.html'


# Vues du modèle Métacatégories
class MetacategorieListView(ListView):
    """Liste des comptes créés"""
    model = Metacategorie
    template_name = 'comptes/metacategories_list.html'


class MetacategorieCreateView(CreateView):
    """Création d'un compte"""
    model = Compte
    template_name = 'comptes/metacategorie_create.html'


class MetacategorieUpdateView(UpdateView):
    """Mise à jour d'un compte"""
    model = Compte
    template_name = 'comptes/metacategorie_create.html'
