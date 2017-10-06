from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings
from PIL import Image
import os
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Points"


class Badges(models.Model):
   badge_title = models.CharField(max_length=50)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   points_needed = models.IntegerField(default=0)
   badge_image = models.CharField(max_length=1000)
   def __str__(self):
       return self.badge_title
   class Meta:
       verbose_name_plural = "Badges"