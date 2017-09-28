# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_english', models.CharField(max_length=30)),
                ('category_french', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('English', models.CharField(max_length=20)),
                ('French', models.IntegerField(default=0)),
                ('Image', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(to='LingoLearn.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SP_total', models.IntegerField(default=0)),
                ('MP_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.ForeignKey(to='LingoLearn.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('full_name', models.CharField(max_length=100)),
                ('singleP', models.IntegerField(default=0)),
                ('multiP', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='points',
            name='user',
            field=models.ForeignKey(to='LingoLearn.User'),
        ),
        migrations.AddField(
            model_name='leaderboard',
            name='user',
            field=models.ForeignKey(to='LingoLearn.User'),
        ),
    ]
