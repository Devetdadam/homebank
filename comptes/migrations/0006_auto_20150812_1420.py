# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0005_ligne_mois'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligne',
            name='mois',
            field=models.IntegerField(choices=[(201501, '2015 Janvier'), (201502, '2015 F\xe9vrier'), (201503, '2015 Mars')]),
        ),
    ]
