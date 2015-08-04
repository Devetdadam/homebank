# coding: utf8

from django.contrib import admin
from .models import Metacategorie, Categorie, Ligne, Compte

admin.site.register(Metacategorie)
admin.site.register(Categorie)
admin.site.register(Compte)
admin.site.register(Ligne)
