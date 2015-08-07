# coding: utf8
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .models import Compte, Categorie
# from .forms import CompteForm


# Page d'Accueil
class AccueilTemplateView(TemplateView):
    """page d'accueil de l'application"""
    template_name = "accueil.html"


class AdministrationListView(ListView):
    context_object_name = 'administration_list'
    template_name = 'administration.html'
    context_object_name = 'comptes_list'

    def get_queryset(self):
        self.proprietaire = get_object_or_404(User, id=self.request.user.id)
        return Compte.objects.filter(proprietaire=self.proprietaire)

    def get_context_data(self, **kwargs):
        context = super(AdministrationListView, self).get_context_data(**kwargs)
        self.proprietaire = get_object_or_404(User, id=self.request.user.id)
        context['metacategories_list'] = Categorie.objects.filter(proprietaire=self.proprietaire, ismeta=True)
        context['categories_list'] = Categorie.objects.filter(proprietaire=self.proprietaire, ismeta=False)
        return context


# Vues du modèle Compte
# class CompteListView(ListView):
#     """Liste des comptes créés"""
#     model = Compte
#     context_object_name = 'comptes_list'
#     template_name = 'administration.html'

#     def get_queryset(self):
#         self.proprietaire = get_object_or_404(User, id=self.request.user.id)
#         return Compte.objects.filter(proprietaire=self.proprietaire)


class CompteCreateView(CreateView):
    """Création d'un nouveau compte"""
    model = Compte
    template_name = 'create.html'
    fields = ['compte', 'alias']
    success_url = reverse_lazy('administration')

    # avant d'enregistrer, on implémente le champ 'proprietaire'
    # avec la valeur du user connecté
    def form_valid(self, form):
        user = self.request.user
        form.instance.proprietaire = user
        return super(CompteCreateView, self).form_valid(form)


class CompteUpdateView(UpdateView):
    """Mise à jour d'un compte"""
    model = Compte
    template_name = 'create.html'
    fields = ['compte', 'alias']
    slug_url_kwarg = 'alias'
    slug_field = 'alias'
    success_url = reverse_lazy('administration')


# Vues du modèle Catégorie
# class CategorieListView(ListView):
#     """Liste des catégories créés"""
#     model = Categorie
#     context_object_name = 'categories_list'
#     template_name = 'administration.html'

#     def get_queryset(self):
#         self.proprietaire = get_object_or_404(User, id=self.request.user.id)
#         return Categorie.objects.filter(proprietaire=self.proprietaire)


class CategorieCreateView(CreateView):
    """Création d'une nouvelle catégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['metacategorie', 'categorie']
    success_url = reverse_lazy('administration')

    # avant d'enregistrer, on implémente le champ 'proprietaire'
    # avec la valeur du user connecté
    def form_valid(self, form):
        user = self.request.user
        form.instance.proprietaire = user
        return super(CategorieCreateView, self).form_valid(form)


class CategorieUpdateView(UpdateView):
    """Mise à jour d'une catégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['metacategorie', 'categorie', 'ismeta']
    slug_url_kwarg = 'categorie'
    slug_field = 'categorie'
    success_url = reverse_lazy('administration')
