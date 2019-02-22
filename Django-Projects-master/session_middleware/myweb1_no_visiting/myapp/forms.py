from django import forms


class contactform(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    







   
