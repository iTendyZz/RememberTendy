from django.contrib import admin
from . import models

# Register your models here.

class MyUserAvatarChange(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")

admin.site.register(models.MyUserAvatar, MyUserAvatarChange)