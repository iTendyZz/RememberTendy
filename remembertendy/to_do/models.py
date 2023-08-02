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

class ToDo(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    description = models.TextField(verbose_name="Текст", blank=True)
    icon = models.ImageField(verbose_name="Медиа", upload_to="to_do/to_dos/%Y/%m/%d", blank=True)
    create_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    complete_date = models.DateTimeField(verbose_name="Дата завершения", null=True, blank=True)
    important = models.BooleanField(verbose_name="Важно", default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="пользователь")

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = "Записи"

    def __str__(self):
        return self.title
    
    