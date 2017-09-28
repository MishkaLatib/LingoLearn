from django.db import models


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

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.category_english


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    English = models.CharField(max_length=30)
    French = models.CharField(max_length=30)
    Image = models.CharField(max_length=1000)


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

