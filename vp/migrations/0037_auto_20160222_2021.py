# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0036_auto_20160221_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mturklocationinfo',
            name='deals',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
