# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0003_auto_20150812_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligne',
            name='mois',
        ),
    ]
