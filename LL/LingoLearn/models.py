from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    singleP = models.IntegerField(default=0)
    multiP = models.IntegerField(default=0)


