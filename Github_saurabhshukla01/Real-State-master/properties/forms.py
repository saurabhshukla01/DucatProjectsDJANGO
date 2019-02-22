from .models import Property

from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('profile','list_date',)
