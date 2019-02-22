from django import forms
from django.contrib.auth.models import User
from .models import *

class Addharform(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Name'}
    ),required=True,max_length=30)

    Email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}
    ),required=True, max_length=30)

    DOB = forms.DateField(input_formats=['%d-%m-%y'])
    
    Gender = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Gender'}
    ),required=True, max_length=30)

    Address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
    ),required=True, max_length=30)

    Parents_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Parents_name'}
    ),required=True, max_length=30)

    Mob_no = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Mob_no'}
    ),required=True, max_length=30)

    class Meta:
        model=User
        fields=['Name','Email','DOB','Gender','Address','Parents_name','Mob_no']

      