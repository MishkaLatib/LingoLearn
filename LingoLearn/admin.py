from django.contrib import admin
from LingoLearn import models


#Category information for Single Player
admin.site.register(models.Category)
admin.site.register(models.Item)
#Points information
admin.site.register(models.Points)

admin.site.register(models.Badges)