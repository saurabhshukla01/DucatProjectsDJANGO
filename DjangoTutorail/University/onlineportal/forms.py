from django import forms
from django.contrib.auth.models import User
from .models import *


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'

    
class proffForm(forms.ModelForm):
    class Meta:
        model = proff_of_university
        fields = '__all__'

class proff_details_Form(forms.ModelForm):
    class Meta:
        model = proff_details
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Applicant Name'}
    ),required=True,max_length=30)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}
    ),required=True, max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First name'}
    ),required=True, max_length=30)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last name'}
    ),required=True, max_length=30)
    Address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
    ),required=True, max_length=30)
    Parents_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Parents name'}
    ),required=True, max_length=30)
    
    age = forms.IntegerField()

    contact_no = forms.IntegerField()

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ),required=True, max_length=30)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}
    ),required=True, max_length=30)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','Address','Parents_name','age','contact_no','password','confirm_password']

    def clean_confirm_password(self):
        p=self.cleaned_data['password']
        cp=self.cleaned_data['confirm_password']
        if(p!=cp):
            raise forms.ValidationError("Confirm Password and Password Must be Same")
        else:
            if(len(p)<8):
                raise forms.ValidationError("Password must be atleast 8 Character")
            if(p.isdigit()):
                raise forms.ValidationError("Password must contains aleast a character")    