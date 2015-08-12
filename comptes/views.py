# coding: utf8
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView, CreateView,\
    UpdateView

from .models import Compte, Categorie


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
        context['metacategories_list'] = Categorie.objects.filter(
            proprietaire=self.proprietaire, ismeta=True
        )
        context['categories_list'] = Categorie.objects.filter(
            proprietaire=self.proprietaire, ismeta=False
        )
        return context


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


class MetacategorieCreateView(CreateView):
    """Création d'une nouvelle métacatégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['categorie']
    success_url = reverse_lazy('administration')

    # # avant d'enregistrer, on implémente le champ 'proprietaire'
    # # avec la valeur du user connecté
    def form_valid(self, form):
        user = self.request.user
        form.instance.proprietaire = user
        form.instance.ismeta = True
        return super(MetacategorieCreateView, self).form_valid(form)


class MetacategorieUpdateView(UpdateView):
    """Mise à jour d'une métacatégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['categorie']
    slug_url_kwarg = 'metacategorie'
    slug_field = 'categorie'
    success_url = reverse_lazy('administration')


class CategorieCreateView(CreateView):
    """Création d'une nouvelle catégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['categorie']
    slug_url_kwarg = 'metacategorie'
    slug_field = 'mecategorie'
    success_url = reverse_lazy('administration')

    def get_object(self):
        return Categorie.objects.get(
            categorie=self.request.GET.get('metacategorie')
        )

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CategorieCreateView, self).get_context_data(**kwargs)
        context['metacategorie'] = get_object_or_404(
            Categorie, categorie=self.kwargs['metacategorie']
        )
        return context

    # avant d'enregistrer, on implémente le champ 'proprietaire'
    # avec la valeur du user connecté
    def form_valid(self, form, **kwargs):
        user = self.request.user
        form.instance.proprietaire = user
        metacategorie = get_object_or_404(
            Categorie, categorie=self.kwargs['metacategorie']
        )
        form.instance.ismeta = False
        form.instance.metacategorie = metacategorie
        return super(CategorieCreateView, self).form_valid(form)


class CategorieUpdateView(UpdateView):
    """Mise à jour d'une catégorie"""
    model = Categorie
    template_name = 'create.html'
    fields = ['categorie']
    slug_url_kwarg = 'categorie'
    slug_field = 'categorie'
    success_url = reverse_lazy('administration')
