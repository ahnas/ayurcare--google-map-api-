from django import forms
from django.db.models import fields
from .models import Branch
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),
            'latitude': TextInput(attrs={'class': 'form-control', 'placeholder': 'latitude'}),
            'longitude': TextInput(attrs={'class': 'form-control', 'placeholder': 'longitude'}),
        }