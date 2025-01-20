from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Receipt(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    cooking_steps = models.TextField(verbose_name="Шаги приготовления")
    cooking_time = models.TimeField(null=True, verbose_name="Время приготовления")
    image = models.ImageField(upload_to='main/static/img/',
                              null=True,
                              blank=True,
                              verbose_name="Изображение")
    author = models.CharField(max_length=50, null=False, verbose_name="Автор")
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"Рецепт {self.id} под названием {self.name}"


