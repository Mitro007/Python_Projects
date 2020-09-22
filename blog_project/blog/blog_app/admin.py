from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'date_posted', 'user']

admin.site.register(models.Post, PostAdmin)