from django import forms
from django.contrib.auth.models import User
from .models import *


class Regforms(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    email=forms.CharField(widget=forms.EmailInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)

    password=forms.CharField(widget=forms.PasswordInput
                             (attrs={'class':'form-control'}),
                             max_length=30,
                             required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput
                            (attrs={'class': 'form-control'}),
                            label="Confirm your password",
                            max_length=30,
                            required=True)
    class Meta:
        model=User
        fields=['username','email','password','confirm_password',]
        
class comment_form(forms.ModelForm):
    class Meta:
        model=comment
        fields=['user_comment']
        
class Postform(forms.Form):
    #title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control','style':'width:300px;'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Say something...!','rows': 4, 'cols': 50, 'style':'resize:none;width:400px;','class':'form-control'}))
    pic = forms.FileField(required=False)

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                 max_length=100,
                                 required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                                 max_length=100,
                                 required=False)

    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                
        max_length=50,
        required=False)
    
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),
                          max_length=30,
                          required=False) 

    location = forms.CharField(
        
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)

    pic = forms.FileField(required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'job_title',
                  'email', 'location','pic' ]


class ChangePasswordForm(forms.ModelForm):
    
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']
