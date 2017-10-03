from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image
import os


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    singleP = models.IntegerField(default=0)
    multiP = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username


class Category(models.Model):
    category_english = models.CharField(max_length=30)
    category_french = models.CharField(max_length=30)
    category_image = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.category_english


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    English = models.CharField(max_length=30)
    French = models.CharField(max_length=30)
    Image = models.CharField(max_length=1000)

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.category, "  :  ", self.English,"-->", self.French)


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Points"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SP_total = models.IntegerField(default=0)
    MP_total = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Leaderboard"


class Badges(models.Model):
   badge_title = models.CharField(max_length=50)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   points_needed = models.IntegerField(default=0)
   badge_image = models.CharField(max_length=1000)
   def __str__(self):
       return self.badge_title
   class Meta:
       verbose_name_plural = "Badges"