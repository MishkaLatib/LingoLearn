from django.db import models
from django.contrib.auth.models import User

#Models which create database tables to be filled, with field type and legnth requirments.


#Category class to keep track of the learning Categories available in the app: i.e Food, The Body...
#Keeps track of Category name, translation and an appropriate image

class Category(models.Model):
    category_english = models.CharField(max_length=30)
    category_french = models.CharField(max_length=30)
    category_image = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.category_english

#Item class which creates Object instances of items linked to a specific category.
#Items include the name, translation and appropriate image
#Single item links to Category, Category can have lots of images

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    English = models.CharField(max_length=30)
    French = models.CharField(max_length=30)
    Image = models.CharField(max_length=1000)

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.category, "  :  ", self.English,"-->", self.French)

#Keeps track of user points

class Points(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Points"

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.user, "  :  ", self.category,"-->", self.points)

#Tracks Badges based on user points

class Badges(models.Model):
   badge_title = models.CharField(max_length=50)
   points_needed = models.IntegerField(default=0)
   badge_image = models.CharField(max_length=1000)
   def __str__(self):
       return self.badge_title
   class Meta:
       verbose_name_plural = "Badges"