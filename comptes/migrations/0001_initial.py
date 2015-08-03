# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categorie', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mois', models.CharField(max_length=20, choices=[(b'2000 Janvier', b'2000 Janvier'), (b'2000 F\xc3\xa9vrier', b'2000 F\xc3\xa9vrier'), (b'2000 Mars', b'2000 Mars'), (b'2000 Avril', b'2000 Avril'), (b'2000 Mai', b'2000 Mai'), (b'2000 Juin', b'2000 Juin'), (b'2000 Juillet', b'2000 Juillet'), (b'2000 Ao\xc3\xbbt', b'2000 Ao\xc3\xbbt'), (b'2000 Septembre', b'2000 Septembre'), (b'2000 Octobre', b'2000 Octobre'), (b'2000 Novembre', b'2000 Novembre'), (b'2000 D\xc3\xa9cembre', b'2000 D\xc3\xa9cembre'), (b'2001 Janvier', b'2001 Janvier'), (b'2001 F\xc3\xa9vrier', b'2001 F\xc3\xa9vrier'), (b'2001 Mars', b'2001 Mars'), (b'2001 Avril', b'2001 Avril'), (b'2001 Mai', b'2001 Mai'), (b'2001 Juin', b'2001 Juin'), (b'2001 Juillet', b'2001 Juillet'), (b'2001 Ao\xc3\xbbt', b'2001 Ao\xc3\xbbt'), (b'2001 Septembre', b'2001 Septembre'), (b'2001 Octobre', b'2001 Octobre'), (b'2001 Novembre', b'2001 Novembre'), (b'2001 D\xc3\xa9cembre', b'2001 D\xc3\xa9cembre'), (b'2002 Janvier', b'2002 Janvier'), (b'2002 F\xc3\xa9vrier', b'2002 F\xc3\xa9vrier'), (b'2002 Mars', b'2002 Mars'), (b'2002 Avril', b'2002 Avril'), (b'2002 Mai', b'2002 Mai'), (b'2002 Juin', b'2002 Juin'), (b'2002 Juillet', b'2002 Juillet'), (b'2002 Ao\xc3\xbbt', b'2002 Ao\xc3\xbbt'), (b'2002 Septembre', b'2002 Septembre'), (b'2002 Octobre', b'2002 Octobre'), (b'2002 Novembre', b'2002 Novembre'), (b'2002 D\xc3\xa9cembre', b'2002 D\xc3\xa9cembre'), (b'2003 Janvier', b'2003 Janvier'), (b'2003 F\xc3\xa9vrier', b'2003 F\xc3\xa9vrier'), (b'2003 Mars', b'2003 Mars'), (b'2003 Avril', b'2003 Avril'), (b'2003 Mai', b'2003 Mai'), (b'2003 Juin', b'2003 Juin'), (b'2003 Juillet', b'2003 Juillet'), (b'2003 Ao\xc3\xbbt', b'2003 Ao\xc3\xbbt'), (b'2003 Septembre', b'2003 Septembre'), (b'2003 Octobre', b'2003 Octobre'), (b'2003 Novembre', b'2003 Novembre'), (b'2003 D\xc3\xa9cembre', b'2003 D\xc3\xa9cembre'), (b'2004 Janvier', b'2004 Janvier'), (b'2004 F\xc3\xa9vrier', b'2004 F\xc3\xa9vrier'), (b'2004 Mars', b'2004 Mars'), (b'2004 Avril', b'2004 Avril'), (b'2004 Mai', b'2004 Mai'), (b'2004 Juin', b'2004 Juin'), (b'2004 Juillet', b'2004 Juillet'), (b'2004 Ao\xc3\xbbt', b'2004 Ao\xc3\xbbt'), (b'2004 Septembre', b'2004 Septembre'), (b'2004 Octobre', b'2004 Octobre'), (b'2004 Novembre', b'2004 Novembre'), (b'2004 D\xc3\xa9cembre', b'2004 D\xc3\xa9cembre'), (b'2005 Janvier', b'2005 Janvier'), (b'2005 F\xc3\xa9vrier', b'2005 F\xc3\xa9vrier'), (b'2005 Mars', b'2005 Mars'), (b'2005 Avril', b'2005 Avril'), (b'2005 Mai', b'2005 Mai'), (b'2005 Juin', b'2005 Juin'), (b'2005 Juillet', b'2005 Juillet'), (b'2005 Ao\xc3\xbbt', b'2005 Ao\xc3\xbbt'), (b'2005 Septembre', b'2005 Septembre'), (b'2005 Octobre', b'2005 Octobre'), (b'2005 Novembre', b'2005 Novembre'), (b'2005 D\xc3\xa9cembre', b'2005 D\xc3\xa9cembre'), (b'2006 Janvier', b'2006 Janvier'), (b'2006 F\xc3\xa9vrier', b'2006 F\xc3\xa9vrier'), (b'2006 Mars', b'2006 Mars'), (b'2006 Avril', b'2006 Avril'), (b'2006 Mai', b'2006 Mai'), (b'2006 Juin', b'2006 Juin'), (b'2006 Juillet', b'2006 Juillet'), (b'2006 Ao\xc3\xbbt', b'2006 Ao\xc3\xbbt'), (b'2006 Septembre', b'2006 Septembre'), (b'2006 Octobre', b'2006 Octobre'), (b'2006 Novembre', b'2006 Novembre'), (b'2006 D\xc3\xa9cembre', b'2006 D\xc3\xa9cembre'), (b'2007 Janvier', b'2007 Janvier'), (b'2007 F\xc3\xa9vrier', b'2007 F\xc3\xa9vrier'), (b'2007 Mars', b'2007 Mars'), (b'2007 Avril', b'2007 Avril'), (b'2007 Mai', b'2007 Mai'), (b'2007 Juin', b'2007 Juin'), (b'2007 Juillet', b'2007 Juillet'), (b'2007 Ao\xc3\xbbt', b'2007 Ao\xc3\xbbt'), (b'2007 Septembre', b'2007 Septembre'), (b'2007 Octobre', b'2007 Octobre'), (b'2007 Novembre', b'2007 Novembre'), (b'2007 D\xc3\xa9cembre', b'2007 D\xc3\xa9cembre'), (b'2008 Janvier', b'2008 Janvier'), (b'2008 F\xc3\xa9vrier', b'2008 F\xc3\xa9vrier'), (b'2008 Mars', b'2008 Mars'), (b'2008 Avril', b'2008 Avril'), (b'2008 Mai', b'2008 Mai'), (b'2008 Juin', b'2008 Juin'), (b'2008 Juillet', b'2008 Juillet'), (b'2008 Ao\xc3\xbbt', b'2008 Ao\xc3\xbbt'), (b'2008 Septembre', b'2008 Septembre'), (b'2008 Octobre', b'2008 Octobre'), (b'2008 Novembre', b'2008 Novembre'), (b'2008 D\xc3\xa9cembre', b'2008 D\xc3\xa9cembre'), (b'2009 Janvier', b'2009 Janvier'), (b'2009 F\xc3\xa9vrier', b'2009 F\xc3\xa9vrier'), (b'2009 Mars', b'2009 Mars'), (b'2009 Avril', b'2009 Avril'), (b'2009 Mai', b'2009 Mai'), (b'2009 Juin', b'2009 Juin'), (b'2009 Juillet', b'2009 Juillet'), (b'2009 Ao\xc3\xbbt', b'2009 Ao\xc3\xbbt'), (b'2009 Septembre', b'2009 Septembre'), (b'2009 Octobre', b'2009 Octobre'), (b'2009 Novembre', b'2009 Novembre'), (b'2009 D\xc3\xa9cembre', b'2009 D\xc3\xa9cembre'), (b'2010 Janvier', b'2010 Janvier'), (b'2010 F\xc3\xa9vrier', b'2010 F\xc3\xa9vrier'), (b'2010 Mars', b'2010 Mars'), (b'2010 Avril', b'2010 Avril'), (b'2010 Mai', b'2010 Mai'), (b'2010 Juin', b'2010 Juin'), (b'2010 Juillet', b'2010 Juillet'), (b'2010 Ao\xc3\xbbt', b'2010 Ao\xc3\xbbt'), (b'2010 Septembre', b'2010 Septembre'), (b'2010 Octobre', b'2010 Octobre'), (b'2010 Novembre', b'2010 Novembre'), (b'2010 D\xc3\xa9cembre', b'2010 D\xc3\xa9cembre'), (b'2011 Janvier', b'2011 Janvier'), (b'2011 F\xc3\xa9vrier', b'2011 F\xc3\xa9vrier'), (b'2011 Mars', b'2011 Mars'), (b'2011 Avril', b'2011 Avril'), (b'2011 Mai', b'2011 Mai'), (b'2011 Juin', b'2011 Juin'), (b'2011 Juillet', b'2011 Juillet'), (b'2011 Ao\xc3\xbbt', b'2011 Ao\xc3\xbbt'), (b'2011 Septembre', b'2011 Septembre'), (b'2011 Octobre', b'2011 Octobre'), (b'2011 Novembre', b'2011 Novembre'), (b'2011 D\xc3\xa9cembre', b'2011 D\xc3\xa9cembre'), (b'2012 Janvier', b'2012 Janvier'), (b'2012 F\xc3\xa9vrier', b'2012 F\xc3\xa9vrier'), (b'2012 Mars', b'2012 Mars'), (b'2012 Avril', b'2012 Avril'), (b'2012 Mai', b'2012 Mai'), (b'2012 Juin', b'2012 Juin'), (b'2012 Juillet', b'2012 Juillet'), (b'2012 Ao\xc3\xbbt', b'2012 Ao\xc3\xbbt'), (b'2012 Septembre', b'2012 Septembre'), (b'2012 Octobre', b'2012 Octobre'), (b'2012 Novembre', b'2012 Novembre'), (b'2012 D\xc3\xa9cembre', b'2012 D\xc3\xa9cembre'), (b'2013 Janvier', b'2013 Janvier'), (b'2013 F\xc3\xa9vrier', b'2013 F\xc3\xa9vrier'), (b'2013 Mars', b'2013 Mars'), (b'2013 Avril', b'2013 Avril'), (b'2013 Mai', b'2013 Mai'), (b'2013 Juin', b'2013 Juin'), (b'2013 Juillet', b'2013 Juillet'), (b'2013 Ao\xc3\xbbt', b'2013 Ao\xc3\xbbt'), (b'2013 Septembre', b'2013 Septembre'), (b'2013 Octobre', b'2013 Octobre'), (b'2013 Novembre', b'2013 Novembre'), (b'2013 D\xc3\xa9cembre', b'2013 D\xc3\xa9cembre'), (b'2014 Janvier', b'2014 Janvier'), (b'2014 F\xc3\xa9vrier', b'2014 F\xc3\xa9vrier'), (b'2014 Mars', b'2014 Mars'), (b'2014 Avril', b'2014 Avril'), (b'2014 Mai', b'2014 Mai'), (b'2014 Juin', b'2014 Juin'), (b'2014 Juillet', b'2014 Juillet'), (b'2014 Ao\xc3\xbbt', b'2014 Ao\xc3\xbbt'), (b'2014 Septembre', b'2014 Septembre'), (b'2014 Octobre', b'2014 Octobre'), (b'2014 Novembre', b'2014 Novembre'), (b'2014 D\xc3\xa9cembre', b'2014 D\xc3\xa9cembre'), (b'2015 Janvier', b'2015 Janvier'), (b'2015 F\xc3\xa9vrier', b'2015 F\xc3\xa9vrier'), (b'2015 Mars', b'2015 Mars'), (b'2015 Avril', b'2015 Avril'), (b'2015 Mai', b'2015 Mai'), (b'2015 Juin', b'2015 Juin'), (b'2015 Juillet', b'2015 Juillet'), (b'2015 Ao\xc3\xbbt', b'2015 Ao\xc3\xbbt'), (b'2015 Septembre', b'2015 Septembre'), (b'2015 Octobre', b'2015 Octobre'), (b'2015 Novembre', b'2015 Novembre'), (b'2015 D\xc3\xa9cembre', b'2015 D\xc3\xa9cembre'), (b'2016 Janvier', b'2016 Janvier'), (b'2016 F\xc3\xa9vrier', b'2016 F\xc3\xa9vrier'), (b'2016 Mars', b'2016 Mars'), (b'2016 Avril', b'2016 Avril'), (b'2016 Mai', b'2016 Mai'), (b'2016 Juin', b'2016 Juin'), (b'2016 Juillet', b'2016 Juillet'), (b'2016 Ao\xc3\xbbt', b'2016 Ao\xc3\xbbt'), (b'2016 Septembre', b'2016 Septembre'), (b'2016 Octobre', b'2016 Octobre'), (b'2016 Novembre', b'2016 Novembre'), (b'2016 D\xc3\xa9cembre', b'2016 D\xc3\xa9cembre'), (b'2017 Janvier', b'2017 Janvier'), (b'2017 F\xc3\xa9vrier', b'2017 F\xc3\xa9vrier'), (b'2017 Mars', b'2017 Mars'), (b'2017 Avril', b'2017 Avril'), (b'2017 Mai', b'2017 Mai'), (b'2017 Juin', b'2017 Juin'), (b'2017 Juillet', b'2017 Juillet'), (b'2017 Ao\xc3\xbbt', b'2017 Ao\xc3\xbbt'), (b'2017 Septembre', b'2017 Septembre'), (b'2017 Octobre', b'2017 Octobre'), (b'2017 Novembre', b'2017 Novembre'), (b'2017 D\xc3\xa9cembre', b'2017 D\xc3\xa9cembre'), (b'2018 Janvier', b'2018 Janvier'), (b'2018 F\xc3\xa9vrier', b'2018 F\xc3\xa9vrier'), (b'2018 Mars', b'2018 Mars'), (b'2018 Avril', b'2018 Avril'), (b'2018 Mai', b'2018 Mai'), (b'2018 Juin', b'2018 Juin'), (b'2018 Juillet', b'2018 Juillet'), (b'2018 Ao\xc3\xbbt', b'2018 Ao\xc3\xbbt'), (b'2018 Septembre', b'2018 Septembre'), (b'2018 Octobre', b'2018 Octobre'), (b'2018 Novembre', b'2018 Novembre'), (b'2018 D\xc3\xa9cembre', b'2018 D\xc3\xa9cembre'), (b'2019 Janvier', b'2019 Janvier'), (b'2019 F\xc3\xa9vrier', b'2019 F\xc3\xa9vrier'), (b'2019 Mars', b'2019 Mars'), (b'2019 Avril', b'2019 Avril'), (b'2019 Mai', b'2019 Mai'), (b'2019 Juin', b'2019 Juin'), (b'2019 Juillet', b'2019 Juillet'), (b'2019 Ao\xc3\xbbt', b'2019 Ao\xc3\xbbt'), (b'2019 Septembre', b'2019 Septembre'), (b'2019 Octobre', b'2019 Octobre'), (b'2019 Novembre', b'2019 Novembre'), (b'2019 D\xc3\xa9cembre', b'2019 D\xc3\xa9cembre'), (b'2020 Janvier', b'2020 Janvier'), (b'2020 F\xc3\xa9vrier', b'2020 F\xc3\xa9vrier'), (b'2020 Mars', b'2020 Mars'), (b'2020 Avril', b'2020 Avril'), (b'2020 Mai', b'2020 Mai'), (b'2020 Juin', b'2020 Juin'), (b'2020 Juillet', b'2020 Juillet'), (b'2020 Ao\xc3\xbbt', b'2020 Ao\xc3\xbbt'), (b'2020 Septembre', b'2020 Septembre'), (b'2020 Octobre', b'2020 Octobre'), (b'2020 Novembre', b'2020 Novembre'), (b'2020 D\xc3\xa9cembre', b'2020 D\xc3\xa9cembre'), (b'2021 Janvier', b'2021 Janvier'), (b'2021 F\xc3\xa9vrier', b'2021 F\xc3\xa9vrier'), (b'2021 Mars', b'2021 Mars'), (b'2021 Avril', b'2021 Avril'), (b'2021 Mai', b'2021 Mai'), (b'2021 Juin', b'2021 Juin'), (b'2021 Juillet', b'2021 Juillet'), (b'2021 Ao\xc3\xbbt', b'2021 Ao\xc3\xbbt'), (b'2021 Septembre', b'2021 Septembre'), (b'2021 Octobre', b'2021 Octobre'), (b'2021 Novembre', b'2021 Novembre'), (b'2021 D\xc3\xa9cembre', b'2021 D\xc3\xa9cembre'), (b'2022 Janvier', b'2022 Janvier'), (b'2022 F\xc3\xa9vrier', b'2022 F\xc3\xa9vrier'), (b'2022 Mars', b'2022 Mars'), (b'2022 Avril', b'2022 Avril'), (b'2022 Mai', b'2022 Mai'), (b'2022 Juin', b'2022 Juin'), (b'2022 Juillet', b'2022 Juillet'), (b'2022 Ao\xc3\xbbt', b'2022 Ao\xc3\xbbt'), (b'2022 Septembre', b'2022 Septembre'), (b'2022 Octobre', b'2022 Octobre'), (b'2022 Novembre', b'2022 Novembre'), (b'2022 D\xc3\xa9cembre', b'2022 D\xc3\xa9cembre'), (b'2023 Janvier', b'2023 Janvier'), (b'2023 F\xc3\xa9vrier', b'2023 F\xc3\xa9vrier'), (b'2023 Mars', b'2023 Mars'), (b'2023 Avril', b'2023 Avril'), (b'2023 Mai', b'2023 Mai'), (b'2023 Juin', b'2023 Juin'), (b'2023 Juillet', b'2023 Juillet'), (b'2023 Ao\xc3\xbbt', b'2023 Ao\xc3\xbbt'), (b'2023 Septembre', b'2023 Septembre'), (b'2023 Octobre', b'2023 Octobre'), (b'2023 Novembre', b'2023 Novembre'), (b'2023 D\xc3\xa9cembre', b'2023 D\xc3\xa9cembre'), (b'2024 Janvier', b'2024 Janvier'), (b'2024 F\xc3\xa9vrier', b'2024 F\xc3\xa9vrier'), (b'2024 Mars', b'2024 Mars'), (b'2024 Avril', b'2024 Avril'), (b'2024 Mai', b'2024 Mai'), (b'2024 Juin', b'2024 Juin'), (b'2024 Juillet', b'2024 Juillet'), (b'2024 Ao\xc3\xbbt', b'2024 Ao\xc3\xbbt'), (b'2024 Septembre', b'2024 Septembre'), (b'2024 Octobre', b'2024 Octobre'), (b'2024 Novembre', b'2024 Novembre'), (b'2024 D\xc3\xa9cembre', b'2024 D\xc3\xa9cembre'), (b'2025 Janvier', b'2025 Janvier'), (b'2025 F\xc3\xa9vrier', b'2025 F\xc3\xa9vrier'), (b'2025 Mars', b'2025 Mars'), (b'2025 Avril', b'2025 Avril'), (b'2025 Mai', b'2025 Mai'), (b'2025 Juin', b'2025 Juin'), (b'2025 Juillet', b'2025 Juillet'), (b'2025 Ao\xc3\xbbt', b'2025 Ao\xc3\xbbt'), (b'2025 Septembre', b'2025 Septembre'), (b'2025 Octobre', b'2025 Octobre'), (b'2025 Novembre', b'2025 Novembre'), (b'2025 D\xc3\xa9cembre', b'2025 D\xc3\xa9cembre'), (b'2026 Janvier', b'2026 Janvier'), (b'2026 F\xc3\xa9vrier', b'2026 F\xc3\xa9vrier'), (b'2026 Mars', b'2026 Mars'), (b'2026 Avril', b'2026 Avril'), (b'2026 Mai', b'2026 Mai'), (b'2026 Juin', b'2026 Juin'), (b'2026 Juillet', b'2026 Juillet'), (b'2026 Ao\xc3\xbbt', b'2026 Ao\xc3\xbbt'), (b'2026 Septembre', b'2026 Septembre'), (b'2026 Octobre', b'2026 Octobre'), (b'2026 Novembre', b'2026 Novembre'), (b'2026 D\xc3\xa9cembre', b'2026 D\xc3\xa9cembre'), (b'2027 Janvier', b'2027 Janvier'), (b'2027 F\xc3\xa9vrier', b'2027 F\xc3\xa9vrier'), (b'2027 Mars', b'2027 Mars'), (b'2027 Avril', b'2027 Avril'), (b'2027 Mai', b'2027 Mai'), (b'2027 Juin', b'2027 Juin'), (b'2027 Juillet', b'2027 Juillet'), (b'2027 Ao\xc3\xbbt', b'2027 Ao\xc3\xbbt'), (b'2027 Septembre', b'2027 Septembre'), (b'2027 Octobre', b'2027 Octobre'), (b'2027 Novembre', b'2027 Novembre'), (b'2027 D\xc3\xa9cembre', b'2027 D\xc3\xa9cembre'), (b'2028 Janvier', b'2028 Janvier'), (b'2028 F\xc3\xa9vrier', b'2028 F\xc3\xa9vrier'), (b'2028 Mars', b'2028 Mars'), (b'2028 Avril', b'2028 Avril'), (b'2028 Mai', b'2028 Mai'), (b'2028 Juin', b'2028 Juin'), (b'2028 Juillet', b'2028 Juillet'), (b'2028 Ao\xc3\xbbt', b'2028 Ao\xc3\xbbt'), (b'2028 Septembre', b'2028 Septembre'), (b'2028 Octobre', b'2028 Octobre'), (b'2028 Novembre', b'2028 Novembre'), (b'2028 D\xc3\xa9cembre', b'2028 D\xc3\xa9cembre'), (b'2029 Janvier', b'2029 Janvier'), (b'2029 F\xc3\xa9vrier', b'2029 F\xc3\xa9vrier'), (b'2029 Mars', b'2029 Mars'), (b'2029 Avril', b'2029 Avril'), (b'2029 Mai', b'2029 Mai'), (b'2029 Juin', b'2029 Juin'), (b'2029 Juillet', b'2029 Juillet'), (b'2029 Ao\xc3\xbbt', b'2029 Ao\xc3\xbbt'), (b'2029 Septembre', b'2029 Septembre'), (b'2029 Octobre', b'2029 Octobre'), (b'2029 Novembre', b'2029 Novembre'), (b'2029 D\xc3\xa9cembre', b'2029 D\xc3\xa9cembre'), (b'2030 Janvier', b'2030 Janvier'), (b'2030 F\xc3\xa9vrier', b'2030 F\xc3\xa9vrier'), (b'2030 Mars', b'2030 Mars'), (b'2030 Avril', b'2030 Avril'), (b'2030 Mai', b'2030 Mai'), (b'2030 Juin', b'2030 Juin'), (b'2030 Juillet', b'2030 Juillet'), (b'2030 Ao\xc3\xbbt', b'2030 Ao\xc3\xbbt'), (b'2030 Septembre', b'2030 Septembre'), (b'2030 Octobre', b'2030 Octobre'), (b'2030 Novembre', b'2030 Novembre'), (b'2030 D\xc3\xa9cembre', b'2030 D\xc3\xa9cembre')])),
                ('libelle', models.CharField(max_length=1000)),
                ('montant', models.DecimalField(max_digits=10, decimal_places=2)),
                ('genre', models.CharField(max_length=6, choices=[('D\xc9BIT', 'D\xc9BIT'), ('CR\xc9DIT', 'CR\xc9DIT')])),
                ('categorie', models.ForeignKey(to='comptes.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Metacategorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('metacategorie', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='categorie',
            name='meta',
            field=models.ForeignKey(to='comptes.Metacategorie'),
        ),
    ]
