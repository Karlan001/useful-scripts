from django.contrib import admin

# Register your models here.
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Person


@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    pass


