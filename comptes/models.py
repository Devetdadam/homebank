# coding: utf8
from django.db import models

from utils import TYPES, DATES


class Metacategorie(models.Model):
    """Regroupement de catégories de dépenses"""
    metacategorie = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s" % (self.metacategorie)


class Categorie(models.Model):
    """Catégories de dépenses"""
    meta = models.ForeignKey(Metacategorie)
    categorie = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s" % (self.categorie)


class Ligne(models.Model):
    """ligne de compte"""
    mois = models.CharField(max_length=20, choices=zip(DATES, DATES))
    libelle = models.CharField(max_length=1000)
    categorie = models.ForeignKey(Categorie)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=6, choices=zip(TYPES, TYPES))
