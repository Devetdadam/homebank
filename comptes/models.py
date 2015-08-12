# coding: utf8
from django.db import models
from django.contrib.auth.models import User

from .functions import *


class Compte(models.Model):
    """Comptes bancaires à suivre"""

    proprietaire = models.ForeignKey(User)
    compte = models.CharField(max_length=250, help_text='Nom de votre compte')
    alias = models.CharField(max_length=250,
                             help_text='Votre compte en un seul mot'
                             )

    def __unicode__(self):
        return "%s" % (self.compte)


class Categorie(models.Model):
    """Catégories de dépenses"""

    proprietaire = models.ForeignKey(User)
    metacategorie = models.ForeignKey(
        'self', related_name='meta', null=True, blank=True
    )
    categorie = models.CharField(max_length=250, help_text='Un seul mot SVP')
    ismeta = models.BooleanField(default='False')

    def __unicode__(self):
        return "%s" % (self.categorie)


class Ligne(models.Model):
    """ligne de compte"""

    compte = models.ForeignKey(Compte)
    mois = models.IntegerField(
        choices=moisChoice(START_YEAR, DELTA), default=moisDefault()
    )
    libelle = models.CharField(max_length=1000)
    categorie = models.ForeignKey(Categorie)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=6, choices=zip(TYPES, TYPES))

    def __unicode__(self):
        return "%s - %s - %s - %s - %.2f" % (
            self.compte.alias,
            self.get_mois_display(),
            self.categorie,
            self.genre,
            self.montant
        )


class Rapport(models.Model):
    """partie commune des rapports"""
    pass

    class Meta:
        abstract = True


class RapportStatique(Rapport):
    """rapports mensuels et annuels"""
    pass


class RapportDynamique(Rapport):
    """rapports paramétrables"""
    pass
