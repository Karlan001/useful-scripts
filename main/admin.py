from django.contrib import admin

# Register your models here.
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Person, Receipt


@admin.register(Person)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Receipt)
class ReceiptsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image"]



