# coding: utf8
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView, CreateView, UpdateView
from .models import Compte
# from .forms import CompteForm


# Page d'Accueil
class AccueilTemplateView(TemplateView):
    """page d'accueil de l'application"""
    template_name = "accueil.html"


# Vues du modèle Compte
class CompteListView(ListView):
    """Liste des comptes créés"""
    model = Compte
    context_object_name = 'comptes_list'
    template_name = 'administration.html'

    def get_queryset(self):
        self.proprietaire = get_object_or_404(User, id=self.request.user.id)
        return Compte.objects.filter(proprietaire=self.proprietaire)


class CompteCreateView(CreateView):
    """Création d'un nouveau compte"""
    model = Compte
    template_name = 'create.html'
    fields = ['compte', 'alias']
    success_url = reverse_lazy('comptes_list')

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
    success_url = reverse_lazy('comptes_list')

    # # on passe en paramètre d'url l'alias
    # def get_object(self, queryset=None):
    #     return Compte.objects.get(alias=self.request.GET.get('alias'))
