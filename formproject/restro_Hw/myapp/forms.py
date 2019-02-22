from django import forms
from django.contrib.auth.models import User
from .models import Restromenudb

class Restroregis(forms.ModelForm):
    User_Name=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Enter Username here:'}),required=True,max_length=30)
    Restaurant_Name=forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Enter Restaurant Name here:'}),required=True,max_length=60)
    Email=forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder':'Enter Email here:'}),required=True,max_length=40)
    Password=forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'Enter Password here:'}),required=True,max_length=30)
    Confirm_Password=forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'Enter Password here:'}),required=True,max_length=30)
    
    class Meta:
        model=User
        fields=['User_Name','Restaurant_Name','Email','Password','Confirm_Password']

class Restromenuform(forms.ModelForm):
    class Meta:
        model=Restromenudb
        fields='__all__'