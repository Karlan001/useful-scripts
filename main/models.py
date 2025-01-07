from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Receipt(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    cooking_steps = models.TextField()
    cooking_time = models.TimeField(null=True)
    image = models.ImageField(upload_to='main/static/img/', null=True, blank=True)
    author = models.CharField(max_length=50, null=False)
