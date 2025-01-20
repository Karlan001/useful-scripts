from django import forms
from django.core.files.storage import FileSystemStorage

from .models import Receipt
from django.shortcuts import render, reverse, redirect


class CreateReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"