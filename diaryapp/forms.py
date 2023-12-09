from django.forms import Textarea, ModelForm, DateField, CharField, Field, DateInput, TextInput

from .models import *


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_title', 'entry_date', 'entry_content']

        widgets = {
            "entry_title": TextInput(attrs={"class": "form-control"}),
            "entry_date": DateInput(attrs={"class": "form-control"}),
            "entry_content": Textarea(attrs={"class": "form-control"}),
        }
