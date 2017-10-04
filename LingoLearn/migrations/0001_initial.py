# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('badge_title', models.CharField(max_length=50)),
                ('points_needed', models.IntegerField(default=0)),
                ('badge_image', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Badges',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_english', models.CharField(max_length=30)),
                ('category_french', models.CharField(max_length=30)),
                ('category_image', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('English', models.CharField(max_length=30)),
                ('French', models.CharField(max_length=30)),
                ('Image', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(to='LingoLearn.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='LingoLearn.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Points',
            },
        ),
        migrations.AddField(
            model_name='badges',
            name='category',
            field=models.ForeignKey(to='LingoLearn.Category'),
        ),
    ]
