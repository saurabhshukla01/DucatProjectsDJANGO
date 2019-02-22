from django import forms
from django.contrib.auth.models import User

class student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    email_id = forms.EmailField(widget=forms.EmailInput(),required=True,max_length=50)
    city = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    marks = forms.CharField(widget=forms.NumberInput(),required=True,max_length=10)
    mob_no = forms.CharField(widget=forms.NumberInput(),required=True,max_length=11)
    exam_name = forms.CharField(widget=forms.TextInput(),required=True,max_length=50)

    class Meta():
        model = User
        fields =['name','email_id','city','marks','mob_no','exam_name']
