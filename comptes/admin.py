# coding: utf8

from django.contrib import admin
from .models import Categorie, Ligne, Compte


class LigneAdmin(admin.ModelAdmin):
    fields = ('compte', 'mois', 'libelle', 'categorie', 'montant', 'genre')

admin.site.register(Categorie)
admin.site.register(Compte)
admin.site.register(Ligne, LigneAdmin)
