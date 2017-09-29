from django.contrib import admin
from LingoLearn import models


# Game User information
admin.site.register(models.User)

#Category information for Single Player
admin.site.register(models.Category)
admin.site.register(models.Item)
#Points information
admin.site.register(models.Points)

