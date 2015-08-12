# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0006_auto_20150812_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligne',
            name='mois',
            field=models.IntegerField(default=(201508, '2015 Ao\xfbt'), choices=[(201001, '2010 Janvier'), (201002, '2010 F\xe9vrier'), (201003, '2010 Mars'), (201004, '2010 Avril'), (201005, '2010 Mai'), (201006, '2010 Juin'), (201007, '2010 Juillet'), (201008, '2010 Ao\xfbt'), (201009, '2010 Septembre'), (201010, '2010 Octobre'), (201011, '2010 Novembre'), (201012, '2010 D\xe9cembre'), (201101, '2011 Janvier'), (201102, '2011 F\xe9vrier'), (201103, '2011 Mars'), (201104, '2011 Avril'), (201105, '2011 Mai'), (201106, '2011 Juin'), (201107, '2011 Juillet'), (201108, '2011 Ao\xfbt'), (201109, '2011 Septembre'), (201110, '2011 Octobre'), (201111, '2011 Novembre'), (201112, '2011 D\xe9cembre'), (201201, '2012 Janvier'), (201202, '2012 F\xe9vrier'), (201203, '2012 Mars'), (201204, '2012 Avril'), (201205, '2012 Mai'), (201206, '2012 Juin'), (201207, '2012 Juillet'), (201208, '2012 Ao\xfbt'), (201209, '2012 Septembre'), (201210, '2012 Octobre'), (201211, '2012 Novembre'), (201212, '2012 D\xe9cembre'), (201301, '2013 Janvier'), (201302, '2013 F\xe9vrier'), (201303, '2013 Mars'), (201304, '2013 Avril'), (201305, '2013 Mai'), (201306, '2013 Juin'), (201307, '2013 Juillet'), (201308, '2013 Ao\xfbt'), (201309, '2013 Septembre'), (201310, '2013 Octobre'), (201311, '2013 Novembre'), (201312, '2013 D\xe9cembre'), (201401, '2014 Janvier'), (201402, '2014 F\xe9vrier'), (201403, '2014 Mars'), (201404, '2014 Avril'), (201405, '2014 Mai'), (201406, '2014 Juin'), (201407, '2014 Juillet'), (201408, '2014 Ao\xfbt'), (201409, '2014 Septembre'), (201410, '2014 Octobre'), (201411, '2014 Novembre'), (201412, '2014 D\xe9cembre'), (201501, '2015 Janvier'), (201502, '2015 F\xe9vrier'), (201503, '2015 Mars'), (201504, '2015 Avril'), (201505, '2015 Mai'), (201506, '2015 Juin'), (201507, '2015 Juillet'), (201508, '2015 Ao\xfbt'), (201509, '2015 Septembre'), (201510, '2015 Octobre'), (201511, '2015 Novembre'), (201512, '2015 D\xe9cembre'), (201601, '2016 Janvier'), (201602, '2016 F\xe9vrier'), (201603, '2016 Mars'), (201604, '2016 Avril'), (201605, '2016 Mai'), (201606, '2016 Juin'), (201607, '2016 Juillet'), (201608, '2016 Ao\xfbt'), (201609, '2016 Septembre'), (201610, '2016 Octobre'), (201611, '2016 Novembre'), (201612, '2016 D\xe9cembre'), (201701, '2017 Janvier'), (201702, '2017 F\xe9vrier'), (201703, '2017 Mars'), (201704, '2017 Avril'), (201705, '2017 Mai'), (201706, '2017 Juin'), (201707, '2017 Juillet'), (201708, '2017 Ao\xfbt'), (201709, '2017 Septembre'), (201710, '2017 Octobre'), (201711, '2017 Novembre'), (201712, '2017 D\xe9cembre'), (201801, '2018 Janvier'), (201802, '2018 F\xe9vrier'), (201803, '2018 Mars'), (201804, '2018 Avril'), (201805, '2018 Mai'), (201806, '2018 Juin'), (201807, '2018 Juillet'), (201808, '2018 Ao\xfbt'), (201809, '2018 Septembre'), (201810, '2018 Octobre'), (201811, '2018 Novembre'), (201812, '2018 D\xe9cembre'), (201901, '2019 Janvier'), (201902, '2019 F\xe9vrier'), (201903, '2019 Mars'), (201904, '2019 Avril'), (201905, '2019 Mai'), (201906, '2019 Juin'), (201907, '2019 Juillet'), (201908, '2019 Ao\xfbt'), (201909, '2019 Septembre'), (201910, '2019 Octobre'), (201911, '2019 Novembre'), (201912, '2019 D\xe9cembre'), (202001, '2020 Janvier'), (202002, '2020 F\xe9vrier'), (202003, '2020 Mars'), (202004, '2020 Avril'), (202005, '2020 Mai'), (202006, '2020 Juin'), (202007, '2020 Juillet'), (202008, '2020 Ao\xfbt'), (202009, '2020 Septembre'), (202010, '2020 Octobre'), (202011, '2020 Novembre'), (202012, '2020 D\xe9cembre')]),
        ),
    ]
