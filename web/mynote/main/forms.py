from django import forms
from django.utils import timezone

class AddNewNote(forms.Form):
    category = forms.CharField(label = "Category", max_length=200)
    tag = forms.CharField(label = "Tag", max_length=200)
    link = forms.URLField(label = "Url")
    content = forms.CharField(label = "content", max_length=3000)
    modify_date = timezone.now()