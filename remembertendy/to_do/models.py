from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUserAvatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")
    icon = models.ImageField(verbose_name="Аватарки", upload_to=f"to_do/avatars", default="to_do/avatars/default_icon.jpeg")

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.user.username