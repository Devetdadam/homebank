# coding: utf8

TYPES = (
    u'DÉBIT',
    u'CRÉDIT'
)

MONTHS = (
    (1, 'Janvier'),
    (2, 'Février'),
    (3, 'Mars'),
    (4, 'Avril'),
    (5, 'Mai'),
    (6, 'Juin'),
    (7, 'Juillet'),
    (8, 'Août'),
    (9, 'Septembre'),
    (10, 'Octobre'),
    (11, 'Novembre'),
    (12, 'Décembre'),
)

DATES = [2001]


def moisChoice(debut, duree):
    '''Établit la liste des mois disponibles pour les comptes
    en fonction de START_YEAR et DELTA du fichier settings'''
    liste = []
    for y in [debut+n for n in xrange(duree+1)]:
        for m in xrange(len(MONTHS)):
            liste.append(((y, MONTHS[m][0]), (y, MONTHS[m][1])))
    return liste
