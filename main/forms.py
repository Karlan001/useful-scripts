from django import forms
from .models import Receipt
from django.core import validators


class CreateReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "name", "description", "cooking_steps", "image", "author", "cooking_time"
    # name = forms.CharField(max_length=128)
    # description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}),
    #                                       label='Input description',
    #                                       validators=[validators.RegexValidator(
    #                                           regex=r'great',
    #                                           message='Field must contain word "great"'
    #                                       )],
    #                                       )
    # cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 5}),
    #                                       label='Input description',
    #                                       validators=[validators.RegexValidator(
    #                                           regex=r'great',
    #                                           message='Field must contain word "great"'
    #                                       )],
    #                                       )
    # image = forms.ImageField()
    # author = forms.CharField()
    # cooking_time = forms.TimeField(input_formats='%H:%M')
