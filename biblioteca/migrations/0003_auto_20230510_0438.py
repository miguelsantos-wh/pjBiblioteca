# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20211207_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True),
        ),
    ]
