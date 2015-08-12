# coding: utf8
from datetime import date

START_YEAR = 2010

DELTA = 10

TYPES = (
    u'DÉBIT',
    u'CRÉDIT'
)

MONTHS = (
    (1, u'Janvier'),
    (2, u'Février'),
    (3, u'Mars'),
    (4, u'Avril'),
    (5, u'Mai'),
    (6, u'Juin'),
    (7, u'Juillet'),
    (8, u'Août'),
    (9, u'Septembre'),
    (10, u'Octobre'),
    (11, u'Novembre'),
    (12, u'Décembre'),
)


def moisChoice(debut, duree):
    '''Établit la liste des mois disponibles pour les comptes
    en fonction de START_YEAR et DELTA du fichier settings'''

    liste = []
    for y in [debut+n for n in xrange(duree+1)]:
        for m in xrange(len(MONTHS)):
            liste.append((y*100+MONTHS[m][0], (str(y)+u' '+MONTHS[m][1])))
    return liste


def moisDefault():
    '''Renvoit la valeur de moisChoice adaptée à la date du jour'''
    today = date.today()
    d = today.year*100 + today.month
    l = [m for m in moisChoice(START_YEAR, DELTA) if d in m]
    return l[0][0]
