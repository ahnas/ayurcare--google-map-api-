from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import fields
from .models import Branch,Doctor,Schedule,DistrictMap
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput,TimeInput
from django.contrib.admin import widgets 
from django.contrib.auth.models import User


class DistrictMapForm(forms.ModelForm):
    class Meta:
        model = DistrictMap
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'District Name','id':'name','name':'name'}),
            'latitude': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'District latitude','id':'latitude','name':'latitude'}),
            'longitude': TextInput(attrs={'class': 'form-control lon', 'placeholder': 'District longitude','id':'longitude','name':'longitude'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Name',}),
            'title': TextInput(attrs={'class': 'form-control ', 'placeholder': 'Branch Title'}),
            'location': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Location'}),
            'phone': TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch Phone'}),
            'latitude': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'Branch latitude'}),
            'longitude': TextInput(attrs={'class': 'form-control lon', 'placeholder': 'Branch longitude'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'register_number': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Register Number',}),
            'name': TextInput(attrs={'class': 'form-control ', 'placeholder': 'Name'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'qualification': TextInput(attrs={'class': 'form-control lat', 'placeholder': 'Qualification'}),
            
        }


class ScheduleForm(forms.ModelForm): 
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'treatment': TextInput(attrs={'class': 'form-control', 'placeholder': 'treatment',}),
            'branch': Select(attrs={'class': 'form-control ','id':'branid'}),
            'doctor': Select(attrs={'class': 'form-control','id':'doctid',}),
            'slug': TextInput(attrs={'class': 'form-control','id':'slugid',}),
            'start_time': TimeInput(attrs={'class': 'form-control','type':'time',}),
            'end_time': TimeInput(attrs={'class': 'form-control','type':'time'}),

        }



