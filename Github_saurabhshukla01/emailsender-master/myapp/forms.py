from django import forms
from .models import * 
class EmpForm(forms.ModelForm):
	class Meta():
		model=Emp
		fields='__all__'	 
class EmplForm(forms.ModelForm):
	class Meta():
		model=Empl
		fields='__all__'