from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from .models import *

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}),required=True,max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter firts Name'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}),required=True,max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password'}),required=True,max_length=30)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter password again'}),required=True,max_length=30)
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password','confirm_password']
	
	def clean_confirm_password(self):
		p = self.cleaned_data['password']
		cp = self.cleaned_data['confirm_password']
		if(p!=cp):
			raise forms.ValidationError('P and cp must be same')
		else:
			if(len(p)<8):
				raise forms.ValidationError('P must be of atleast 8 char')
			if(p.isdigit()):
				raise forms.ValidationError('P must be alphanumeric')
	
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			ma = validate_email(email)
		except:
			raise forms.ValidationError('Email is not valid')
		return email

class changepasswordform(forms.Form):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter old password'}),required=True,max_length=30)
	new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter new password'}),required=True,max_length=30)
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter again password'}),required=True,max_length=30)
	
	class Meta:
		model = User
		fields = ['old_password','new_password','confirm_password']

class ProfileForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
	location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
	job_title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
	designation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),required=True,max_length=30)
	pic = forms.FileField(required=True)

	class Meta:
		model = User
		fields = ['first_name','last_name','location','job_title','designation','email','pic']


class comment_form(forms.ModelForm):
    class Meta:
        model=comment
        fields=['user_comment']
        
class Postform(forms.Form):
    #title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control','style':'width:300px;'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Say something...!','rows': 4, 'cols': 50, 'style':'resize:none;width:400px;','class':'form-control'}))
    pic = forms.FileField(required=False)

	


