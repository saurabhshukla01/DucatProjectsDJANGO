

from django import forms

# Create your models here.

from django.contrib.auth.models import User

class Myform(forms.ModelForm):
    department = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username','email','department']
    
