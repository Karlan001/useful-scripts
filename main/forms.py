from django import forms
from .models import Receipt


class CreateReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"
