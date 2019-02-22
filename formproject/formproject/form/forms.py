from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class NameForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
        'placeholder':'Enter UserName'}
    ),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 
        'placeholder': 'Enter email'}
    ),required=True, max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
    ),required=True, max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter lastname'}
    ),required=True, max_length=30)
