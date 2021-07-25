from django.contrib import admin
from bookstore import models

# Register your models here.

admin.site.register(models.UserProfile)

admin.site.register(models.Category)
admin.site.register(models.Book)
admin.site.register(models.Store)
admin.site.register(models.News)