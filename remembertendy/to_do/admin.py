from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.MyUserAvatar)
class MyUserAvatarChange(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id", "user")

@admin.register(models.ToDo)
class ToDoChange(admin.ModelAdmin):
    list_display = ('id', 'title', "create_date", 'complete_date', 'user')
    list_display_links = ("id", 'title', 'user')
    readonly_fields = ('create_date',)
