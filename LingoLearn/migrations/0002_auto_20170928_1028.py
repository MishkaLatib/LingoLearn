# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LingoLearn', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaderboard',
            options={'verbose_name_plural': 'Leaderboard'},
        ),
        migrations.AlterModelOptions(
            name='points',
            options={'verbose_name_plural': 'Points'},
        ),
    ]
