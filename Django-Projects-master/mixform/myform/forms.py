from django import forms
from .models import *
from django.contrib.auth.models import *

class Regform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']

        
class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['location','job_title']
